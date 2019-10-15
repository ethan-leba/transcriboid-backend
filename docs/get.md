# Generate Melody

Creates a melody using the probabilistic model, and sends it to the user.

**URL** : `/api/get/`

**Method** : `GET`

## Success Response

**Code** : `200 OK`

**Content examples**

Returns a sequential collection of notes.
**Duration** is the length of the note in whole notes
(e.g. 0.25 is a quarter note).
**Relative value** is the scale degree relative to the key center.
(e.g. if C is the key center, 0 is C, 2 is E, -1 is B)

```json
{
  "notes": [
    { "relative_value": -3, "duration": 0.25 },
    { "relative_value": -2, "duration": 0.5 },
    ...,
    { "relative_value": 0, "duration": 0.25 }
  ]
}
```
