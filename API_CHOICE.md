# API Choice
# API Choice

-Étudiant : Ndeye Mbasse NDIAYE
- API choisie : quotable
- URL base : https://api.quotable.io
- Documentation officielle / README : https://github.com/lukePeavey/quotable
- Auth : None
- Endpoints testés :
  - GET `/random`
  - GET `/quotes`
- Hypothèses de contrat (champs attendus, types, codes) :
  - Le statut HTTP de `/random` doit être 200.
  - Le `Content-Type` doit être `application/json`.
  - Le champ `content` doit exister et être une chaîne de caractères (string).
  - Le champ `author` doit être une chaîne de caractères (string).
  - Le champ `length` doit être un nombre entier (integer).
  - Une route inexistante doit retourner un statut 404.
- Limites / rate limiting connu : Pas de limite stricte indiquée pour un usage raisonnable.
- Risques (instabilité, downtime, CORS, etc.) : Risque de latence réseau variable selon l'hébergement de l'API.
