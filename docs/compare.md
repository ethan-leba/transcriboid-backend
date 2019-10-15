# Compare Melodies

Takes in a users melodies, and compares it with the actual melody. Returns the users melody annotated with which notes are correct or not.

**URL** : `/api/login/`

**Method** : `POST`

**Auth required** : NO

**Data constraints**

```json
{
  "user": "[A collection of notes (the user input)]",
  "actual": "[A collection of notes (the actual melody)]"
}
```

**Data example**

```json
{
  "user": [
    { "relative_value": -3, "duration": 0.25 },
    { "relative_value": -2, "duration": 0.5 },
    { "relative_value": 0, "duration": 0.25 }
  ],
  "actual": [
    { "relative_value": -1, "duration": 0.25 },
    { "relative_value": -2, "duration": 0.5 },
    { "relative_value": 0, "duration": 0.25 }
  ]
}
```

## Success Response

Adds a correctness flag to the user's notes, and returns the actual song along with it.

**Code** : `200 OK`

**Content example**

```json
{
  "corrected": [
    { "relative_value": -3, "duration": 0.25, "correct": false },
    { "relative_value": -2, "duration": 0.5, "correct": true },
    { "relative_value": 0, "duration": 0.25, "correct": true }
  ],
  "actual": [
    { "relative_value": -1, "duration": 0.25 },
    { "relative_value": -2, "duration": 0.5 },
    { "relative_value": 0, "duration": 0.25 }
  ]
}
```

## Error Response

**Condition** : If the JSON is malformed.

**Code** : `400 BAD REQUEST`

**Content** :

```json
{
  "field_errors": ["Unable to parse the JSON."]
}
```
