import pandas as pd


class CivicParser:

    def _split_profile(self, profile: str):

        if not profile:
            return "", ""

        parts = str(profile).split(maxsplit=1)

        gene = parts[0]
        variant = parts[1] if len(parts) > 1 else ""

        return gene, variant

    def _clean(self, value):

        if pd.isna(value):
            return ""

        return str(value)

    def parse_evidence(self, row):

        profile = self._clean(
            row.get("molecular_profile")
        )

        gene, variant = self._split_profile(profile)

        return {

            "gene": gene,

            "variant": variant,

            "molecular_profile": profile,

            "disease": self._clean(
                row.get("disease")
            ),

            "therapy": self._clean(
                row.get("therapies")
            ),

            "evidence_type": self._clean(
                row.get("evidence_type")
            ),

            "evidence_level": self._clean(
                row.get("evidence_level")
            ),

            "direction": self._clean(
                row.get("evidence_direction")
            ),

            "source": "CIViC"

        }

    def parse_assertion(self, row):

        profile = self._clean(
            row.get("molecular_profile")
        )

        gene, variant = self._split_profile(profile)

        return {

            "gene": gene,

            "variant": variant,

            "molecular_profile": profile,

            "disease": self._clean(
                row.get("disease")
            ),

            "therapy": self._clean(
                row.get("therapies")
            ),

            "assertion_type": self._clean(
                row.get("assertion_type")
            ),

            "significance": self._clean(
                row.get("significance")
            ),

            "source": "CIViC"

        }