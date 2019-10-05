from card_identifier.cardutils import format_card
from card_identifier.cardutils import validate_card
from card_identifier.card_type import identify_card_type
from card_identifier.card_issuer import identify_card_issuer

import json

card="5401683100112371"

a=identify_card_issuer(card)

return json.dumps(a)