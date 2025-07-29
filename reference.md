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
from murf import Murf

client = Murf(
    api_key="YOUR_API_KEY",
)
client.text_to_speech.generate(
    format="MP3",
    sample_rate=44100.0,
    text="Hello, world!",
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

**voice_id:** `str` — Use the GET /v1/speech/voices API to find supported voiceIds. You can use either the voiceId (e.g. en-US-natalie) or just the voice actor's name (e.g. natalie).
    
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

**encoded_as_base_64_with_zero_retention:** `typing.Optional[bool]` — Set to true to receive audio in response as a Base64 encoded string with zero data retention
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` — Format of the generated audio file. Valid values: MP3, WAV, FLAC, ALAW, ULAW, PCM, OGG
    
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
Valid values: "en-US", "en-UK", "es-ES", etc. Use the GET /v1/speech/voices endpoint to retrieve the list of available voices and languages.
    
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

**word_durations_as_original_text:** `typing.Optional[bool]` — If set to true, the word durations in response will return words as the original input text. (English only)
    
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

<details><summary><code>client.text_to_speech.<a href="src/murf/text_to_speech/client.py">stream</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a streaming output of generated audio
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
client.text_to_speech.stream()

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

**voice_id:** `str` — Use the GET /v1/speech/voices API to find supported voiceIds. You can use either the voiceId (e.g. en-US-natalie) or just the voice actor's name (e.g. natalie).
    
</dd>
</dl>

<dl>
<dd>

**channel_type:** `typing.Optional[str]` — Valid values: STEREO, MONO
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` — Format of the generated audio file. Valid values: MP3, WAV, PCM
    
</dd>
</dl>

<dl>
<dd>

**multi_native_locale:** `typing.Optional[str]` 

Specifies the language for the generated audio, enabling a voice to speak in multiple languages natively. Only available in the Gen2 model.
Valid values: "en-US", "en-UK", "es-ES", etc. Use the GET /v1/speech/voices endpoint to retrieve the list of available voices and languages.
    
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.
    
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

## Text
<details><summary><code>client.text.<a href="src/murf/text/client.py">translate</a>(...)</code></summary>
<dl>
<dd>

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
client.text.translate(
    target_language="es-ES",
    texts=["Hello, world.", "How are you?"],
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

**target_language:** `str` — The language code for the target translation
    
</dd>
</dl>

<dl>
<dd>

**texts:** `typing.Sequence[str]` — List of texts to translate
    
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

## VoiceChanger
<details><summary><code>client.voice_changer.<a href="src/murf/voice_changer/client.py">convert</a>(...)</code></summary>
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
from murf import Murf

client = Murf(
    api_key="YOUR_API_KEY",
)
client.voice_changer.convert(
    voice_id="voice_id",
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

**voice_id:** `str` — Use the GET /v1/speech/voices API to find supported voiceIds. You can use either the voiceId (e.g. en-US-natalie) or just the voice actor's name (e.g. natalie).
    
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

**encode_output_as_base_64:** `typing.Optional[bool]` — Set to true to receive audio in response as a Base64 encoded string along with a url.
    
</dd>
</dl>

<dl>
<dd>

**file:** `from __future__ import annotations

typing.Optional[core.File]` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**file_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `typing.Optional[str]` — Format of the generated audio file. Valid values: MP3, WAV, FLAC, ALAW, ULAW
    
</dd>
</dl>

<dl>
<dd>

**multi_native_locale:** `typing.Optional[str]` 

Specifies the language for the generated audio, enabling a voice to speak in multiple languages natively. Only available in the Gen2 model.
Valid values: "en-US", "en-UK", "es-ES", etc.

Use the GET /v1/speech/voices endpoint to retrieve the list of available voices and languages.
    
</dd>
</dl>

<dl>
<dd>

**pitch:** `typing.Optional[int]` — Pitch of the voiceover
    
</dd>
</dl>

<dl>
<dd>

**pronunciation_dictionary:** `typing.Optional[str]` 

A JSON string that defines custom pronunciations for specific words or phrases. Each key is a word or phrase, and its value is an object with `type` and `pronunciation`.

Example 1: '{"live": {"type": "IPA", "pronunciation": "laɪv"}}'

Example 2: '{"2022": {"type": "SAY_AS", "pronunciation": "twenty twenty two"}}'
    
</dd>
</dl>

<dl>
<dd>

**rate:** `typing.Optional[int]` — Speed of the voiceover
    
</dd>
</dl>

<dl>
<dd>

**retain_accent:** `typing.Optional[bool]` — Set to true to retain the original accent of the speaker during voice generation.
    
</dd>
</dl>

<dl>
<dd>

**retain_prosody:** `typing.Optional[bool]` — Indicates whether to retain the original prosody (intonation, rhythm, and stress) of the input voice in the generated output.
    
</dd>
</dl>

<dl>
<dd>

**return_transcription:** `typing.Optional[bool]` — Set to true to include a textual transcription of the generated audio in the response.
    
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

**transcription:** `typing.Optional[str]` — This parameter allows specifying a transcription of the audio clip, which will then be used as input for the voice changer
    
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

## Dubbing Languages
<details><summary><code>client.dubbing.languages.<a href="src/murf/dubbing/languages/client.py">list_destination_languages</a>()</code></summary>
<dl>
<dd>

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
client.dubbing.languages.list_destination_languages()

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

<details><summary><code>client.dubbing.languages.<a href="src/murf/dubbing/languages/client.py">list_source_languages</a>()</code></summary>
<dl>
<dd>

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
client.dubbing.languages.list_source_languages()

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

## Dubbing Jobs
<details><summary><code>client.dubbing.jobs.<a href="src/murf/dubbing/jobs/client.py">create</a>(...)</code></summary>
<dl>
<dd>

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
client.dubbing.jobs.create(
    target_locales=["target_locales"],
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

**target_locales:** `typing.List[str]` — List of target locales
    
</dd>
</dl>

<dl>
<dd>

**file:** `from __future__ import annotations

typing.Optional[core.File]` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**file_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**source_locale:** `typing.Optional[str]` — Source locale
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**file_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[JobsCreateRequestPriority]` — Priority of the job. Allowed values: LOW, NORMAL, HIGH
    
</dd>
</dl>

<dl>
<dd>

**webhook_secret:** `typing.Optional[str]` 
    
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

<details><summary><code>client.dubbing.jobs.<a href="src/murf/dubbing/jobs/client.py">create_with_project_id</a>(...)</code></summary>
<dl>
<dd>

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
client.dubbing.jobs.create_with_project_id(
    project_id="project_id",
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

**project_id:** `str` — Your Project Id
    
</dd>
</dl>

<dl>
<dd>

**file:** `from __future__ import annotations

typing.Optional[core.File]` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**file_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**file_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[JobsCreateWithProjectIdRequestPriority]` — Priority of the job. Allowed values: LOW, NORMAL, HIGH
    
</dd>
</dl>

<dl>
<dd>

**webhook_secret:** `typing.Optional[str]` 
    
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

<details><summary><code>client.dubbing.jobs.<a href="src/murf/dubbing/jobs/client.py">get_status</a>(...)</code></summary>
<dl>
<dd>

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
client.dubbing.jobs.get_status(
    job_id="job_id",
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

**job_id:** `str` 
    
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

## Dubbing Projects
<details><summary><code>client.dubbing.projects.<a href="src/murf/dubbing/projects/client.py">create</a>(...)</code></summary>
<dl>
<dd>

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
client.dubbing.projects.create(
    name="name",
    dubbing_type="AUTOMATED",
    target_locales=["target_locales"],
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

**name:** `str` — Your Project Name
    
</dd>
</dl>

<dl>
<dd>

**dubbing_type:** `ApiCreateProjectRequestDubbingType` 
    
</dd>
</dl>

<dl>
<dd>

**target_locales:** `typing.Sequence[str]` — List of target locales
    
</dd>
</dl>

<dl>
<dd>

**source_locale:** `typing.Optional[str]` — Source Locale
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
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

<details><summary><code>client.dubbing.projects.<a href="src/murf/dubbing/projects/client.py">list</a>(...)</code></summary>
<dl>
<dd>

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
client.dubbing.projects.list()

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

**limit:** `typing.Optional[int]` — Number of Projects in response
    
</dd>
</dl>

<dl>
<dd>

**next:** `typing.Optional[str]` — Next Page Iterator
    
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

<details><summary><code>client.dubbing.projects.<a href="src/murf/dubbing/projects/client.py">update</a>(...)</code></summary>
<dl>
<dd>

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
client.dubbing.projects.update(
    project_id="project_id",
    target_locales=["target_locales"],
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

**project_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**target_locales:** `typing.Sequence[str]` — List of target locales
    
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

