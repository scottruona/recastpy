> [!NOTE]
> Recast.AI was [acquired by SAP](https://web.archive.org/web/20180123215837/https://news.sap.com/sap-powers-innovation-france-acquires-recastai/) and no longer exists.

# recastpy
An unofficial, minimal Python wrapper for the [Recast.AI](https://web.archive.org/web/20180224041630/https://recast.ai/#expand) API. Recast.AI is a natual language parser.

## Dependency
`pip install requests`

## Usage
```python
import recastpy

# Create API object
recast = recastpy.Recast('YOUR ACCESS TOKEN')

# Send text or voice data
text_response = recast.text_request('How do I use recast.ai?')
voice_response = recast.voice_request(open('my_voice_file.wav', mode='rb'))

# Receive JSON!
print(text_response.json)
>> {
    "source": "How do I use recast.ai?",
    "intents": [],
    "sentences": [
        {
            "source": "How do I use recast.ai?",
            "type": "how",
            "action": "do use",
            "agent": "i",
            "polarity": "positive",
            "entities": {
                "pronoun": [
                    {
                        "value": "i",
                        "raw": "I"
                    }
                ],
                "url": [
                    {
                        "value": "recast.ai",
                        "raw": "recast.ai"
                    }
                ]
            }
        }
    ],
    "version": "0.1.4",
    "timestamp": "2016-04-23T05:45:20+02:00",
    "status": 200
}
```


## To-Do

- [ ] Implement all endpoints
- [ ] Implement streaming voice?
- [ ] Add helper attributes to RequestResponse class 
