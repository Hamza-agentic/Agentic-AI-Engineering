class KeywordClassifier:
    """Alternative classifier implementation."""

    def classify(
        self,
        text: str,
    ) -> str:

        text = text.strip().lower()

        if "login" in text:
            return "account"

        if "password" in text:
            return "account"

        if "voucher" in text:
            return "finance"

        if "payment" in text:
            return "finance"

        if "network" in text:
            return "technical"

        if "server" in text:
            return "technical"

        return "other"
    