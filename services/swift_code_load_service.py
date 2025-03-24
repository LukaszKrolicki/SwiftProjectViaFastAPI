import csv
from sqlalchemy.orm import Session
from models.swift_code import SwiftCode


def load_swift_codes_from_csv(db: Session, csv_path: str):
    with open(csv_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        headquarters_map = {}

        for row in reader:
            country_iso2 = row[0].strip().upper()
            swift_code = row[1].strip()
            bank_name = row[3].strip()
            address = row[4].strip()
            country_name = row[7].strip().upper()

            is_headquarter = swift_code.endswith("XXX")

            if is_headquarter:
                hq = SwiftCode(
                    swift_code=swift_code,
                    bank_name=bank_name,
                    address=address,
                    country_iso2=country_iso2,
                    country_name=country_name,
                    is_headquarter=True
                )
                db.add(hq)
                headquarters_map[swift_code] = hq

        db.commit()

        with open(csv_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                swift_code = row[1].strip()

                if not swift_code.endswith("XXX"):
                    headquarter_code = swift_code[:8] + "XXX"
                    hq = headquarters_map.get(headquarter_code)

                    branch = SwiftCode(
                        swift_code=swift_code,
                        bank_name=row[3].strip(),
                        address=row[4].strip(),
                        country_iso2=row[0].strip().upper(),
                        country_name=row[7].strip().upper(),
                        is_headquarter=False,
                        headquarter=hq
                    )
                    db.add(branch)

            db.commit()
