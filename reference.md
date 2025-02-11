# Reference
## Auth
<details><summary><code>client.auth.<a href="src/murf/auth/client.py">generate_token</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates an auth token for authenticating your requests
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from murf import Murf

client = Murf(
    api_key="YOUR_API_KEY",
)
client.auth.generate_token()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## TextToSpeech
<details><summary><code>client.text_to_speech.<a href="src/murf/text_to_speech/client.py">generate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a url to the generated audio file along with other associated properties.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from murf import Murf, PronunciationDetail

client = Murf(
    api_key="YOUR_API_KEY",
)
client.text_to_speech.generate(
    pronunciation_dictionary={
        "2010": PronunciationDetail(
            pronunciation="two thousand and ten",
            type="SAY_AS",
        ),
        "live": PronunciationDetail(
            pronunciation="laɪv",
            type="IPA",
        ),
    },
    text="The 2010 world cup was held in South Africa",
    voice_id="en-US-natalie",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**text:** `str` — The text that is to be synthesised. e.g. 'Hello there [pause 1s] friend'
    
</dd>
</dl>

<dl>
<dd>

**voice_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**audio_duration:** `typing.Optional[float]` — This parameter allows specifying the duration (in seconds) for the generated audio. If the value is 0, this parameter will be ignored. Only available for Gen2 model.
    
</dd>
</dl>

<dl>
<dd>

**channel_type:** `typing.Optional[str]` — Valid values: STEREO, MONO
    
</dd>
</dl>

<dl>
<dd>

**encode_as_base_64:** `typing.Optional[bool]` — Set to true to receive audio in response as a Base64 encoded string instead of a url.
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` — Format of the generated audio file. Valid values: MP3, WAV, FLAC, ALAW, ULAW
    
</dd>
</dl>

<dl>
<dd>

**model_version:** `typing.Optional[GenerateSpeechRequestModelVersion]` — Valid values: GEN1, GEN2. Use GEN2 to generate audio using new and advanced model. Outputs from Gen 2 will sound better, but different from the old model
    
</dd>
</dl>

<dl>
<dd>

**multi_native_locale:** `typing.Optional[str]` 

Specifies the language for the generated audio, enabling a voice to speak in multiple languages natively. Only available in the Gen2 model.
Valid values: "en-US", "en-UK", "es-ES", etc. Use the GET /v1/speed/voices endpoint to retrieve the list of available voices and languages.
    
</dd>
</dl>

<dl>
<dd>

**pitch:** `typing.Optional[int]` — Pitch of the voiceover
    
</dd>
</dl>

<dl>
<dd>

**pronunciation_dictionary:** `typing.Optional[typing.Dict[str, PronunciationDetail]]` 

An object used to define custom pronunciations. 

 Example 1: {"live":{"type": "IPA", "pronunciation": "laɪv"}}. 

 Example 2: {"2022":{"type": "SAY_AS", "pronunciation": "twenty twenty two"}}
    
</dd>
</dl>

<dl>
<dd>

**rate:** `typing.Optional[int]` — Speed of the voiceover
    
</dd>
</dl>

<dl>
<dd>

**sample_rate:** `typing.Optional[float]` — Valid values are 8000, 24000, 44100, 48000
    
</dd>
</dl>

<dl>
<dd>

**style:** `typing.Optional[str]` — The voice style to be used for voiceover generation.
    
</dd>
</dl>

<dl>
<dd>

**variation:** `typing.Optional[int]` — Higher values will add more variation in terms of Pause, Pitch, and Speed to the voice. Only available for Gen2 model.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.text_to_speech.<a href="src/murf/text_to_speech/client.py">get_voices</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of available voices for speech synthesis
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from murf import Murf

client = Murf(
    api_key="YOUR_API_KEY",
)
client.text_to_speech.get_voices()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**token:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

