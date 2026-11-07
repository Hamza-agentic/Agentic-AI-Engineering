from ai_service.classifiers.rule_classifier import RuleClassifier
from ai_service.classifiers.keyword_classifier import KeywordClassifier


def test_password_classification():
    classifier = RuleClassifier()

    result = classifier.classify("I forgot my password")

    assert result == "account"


def test_fee_classification():
    classifier = RuleClassifier()

    result = classifier.classify("I have a fee problem")

    assert result == "finance"


def test_technical_classification():
    classifier = RuleClassifier()

    result = classifier.classify("The server is down")

    assert result == "technical"


def test_unknown_classification():
    classifier = RuleClassifier()

    result = classifier.classify("I want some information")

    assert result == "other"


# ---- KeywordClassifier tests ----

def test_keyword_login_classification():
    classifier = KeywordClassifier()

    result = classifier.classify("I cannot login to my portal")

    assert result == "account"


def test_keyword_password_uppercase_classification():
    classifier = KeywordClassifier()

    result = classifier.classify("I FORGOT MY PASSWORD")

    assert result == "account"


def test_keyword_voucher_classification():
    classifier = KeywordClassifier()

    result = classifier.classify("My voucher is missing")

    assert result == "finance"


def test_keyword_payment_classification():
    classifier = KeywordClassifier()

    result = classifier.classify("The payment failed")

    assert result == "finance"


def test_keyword_network_classification():
    classifier = KeywordClassifier()

    result = classifier.classify("The network is very slow")

    assert result == "technical"


def test_keyword_unknown_classification():
    classifier = KeywordClassifier()

    result = classifier.classify("I want some information")

    assert result == "other"