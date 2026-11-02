# Murf Python SDK

![Murf AI Logo](https://murf.ai/public-assets/home/Murf_Logo.png)

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2Fmurf-ai%2Fmurf-python-sdk)
[![pypi](https://img.shields.io/pypi/v/murf)](https://pypi.python.org/pypi/murf)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/gist/devgeetech-murf/bbe2c7eb01433f4a151f0fd2be23b1c8/murf-python-sdk.ipynb)

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Getting Started](#getting-started)
  - [Streaming (Falcon 2.1)](#streaming-falcon-21)
  - [Synthesize (Gen 2)](#synthesize-gen-2)
  - [List Voices](#list-voices)
- [Features](#features)
- [Asynchronous Usage](#async-client)
- [Exception Handling](#exception-handling)
- [Advanced Configuration](#advanced)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

The Murf Python SDK integrates with the [Murf API](https://murf.ai/api/docs/introduction/overview) for [text-to-speech](https://murf.ai/text-to-speech). Murf offers two TTS models:

- **Streaming ([Falcon 2.1](https://murf.ai/api/docs/text-to-speech-models/falcon-2-1)):** Real-time, low-latency speech for conversational AI and voice agents (time-to-first-audio under 100ms). Use `client.text_to_speech.stream(...)`.
- **Synthesize ([Gen 2](https://murf.ai/api/docs/text-to-speech-models/gen-2)):** Studio-quality voiceover files with styles, pauses, duration, and variation. Use `client.text_to_speech.generate(...)`. Gen 2 is not available for streaming.

Together they cover 150+ voices across 35 languages. Each model has its own catalog; see the [Voice Library](https://murf.ai/api/docs/voices-styles/voice-library). The SDK supports both synchronous and asynchronous clients.

---

## Installation

Check out the [HTTP API documentation](https://murf.ai/api/docs/introduction/quickstart).

Install the SDK using pip. Streaming playback also needs `pyaudio`, which depends on PortAudio (`brew install portaudio` on macOS):

```bash
pip install murf pyaudio
```

---

## Getting Started

Use [Streaming (Falcon 2.1)](https://murf.ai/api/docs/text-to-speech/streaming) for real-time voice agents, or [Synthesize (Gen 2)](https://murf.ai/api/docs/text-to-speech/synthesize) for a studio voiceover file. See the [Quickstart](https://murf.ai/api/docs/introduction/quickstart) and [TTS overview](https://murf.ai/api/docs/text-to-speech/overview).

### Streaming (Falcon 2.1)

```python
import pyaudio
from murf import Murf, MurfRegion

client = Murf(
    api_key="YOUR_API_KEY",  # Not required if you have set the MURF_API_KEY environment variable
    region=MurfRegion.GLOBAL
)

# For lower latency, specify a region closer to your users
# client = Murf(region=MurfRegion.IN)  # Example: India region

# Audio format settings (must match your API output)
SAMPLE_RATE = 24000
CHANNELS = 1
FORMAT = pyaudio.paInt16

def play_streaming_audio():
    # Get the streaming audio generator
    audio_stream = client.text_to_speech.stream(
        text="Hi, How are you doing today?",
        voice_id="Gordon",
        model="falcon-2.1",
        locale="en-US",
        sample_rate=SAMPLE_RATE,
        format="PCM"
    )

    # Setup audio stream for playback
    pa = pyaudio.PyAudio()
    stream = pa.open(format=FORMAT, channels=CHANNELS, rate=SAMPLE_RATE, output=True)

    try:
        print("Starting audio playback...")
        for chunk in audio_stream:
            if chunk:  # Check if chunk has data
                stream.write(chunk)
    except Exception as e:
        print(f"Error during streaming: {e}")
    finally:
        stream.stop_stream()
        stream.close()
        pa.terminate()
        print("Audio streaming and playback complete!")

if __name__ == "__main__":
    play_streaming_audio()
```

See [HTTP streaming](https://murf.ai/api/docs/text-to-speech/streaming) for regions, formats, and WebSocket streaming.

### Synthesize (Gen 2)

```python
from murf import Murf

client = Murf(
    api_key="YOUR_API_KEY",  # Not required if MURF_API_KEY is set
)
res = client.text_to_speech.generate(
    text="There is much to be said",
    voice_id="Terrell",
    locale="en-US",
)
print(res.audio_file)
```

The response includes a URL to the generated audio file. The file is available for download for 72 hours. See [Synthesize](https://murf.ai/api/docs/text-to-speech/synthesize).

### List Voices

Each model has its own voice catalog. Pass `model` when listing voices: `falcon-2.1` for streaming, `gen2` for synthesis.

```python
from murf import Murf

client = Murf(api_key="YOUR_API_KEY")
streaming_voices = client.text_to_speech.get_voices(model="falcon-2.1")
studio_voices = client.text_to_speech.get_voices(model="gen2")
```

See [List Voices](https://murf.ai/api/docs/api-reference/voices/get-voices) and the [Voice Library](https://murf.ai/api/docs/voices-styles/voice-library).

---

## Features

- **Streaming (Falcon 2.1):** Real-time speech for voice agents and conversational AI. See [Falcon 2.1](https://murf.ai/api/docs/text-to-speech-models/falcon-2-1) and [HTTP streaming](https://murf.ai/api/docs/text-to-speech/streaming).
- **Synthesize (Gen 2):** Studio-quality voiceover files with styles, pauses, duration, and variation. See [Gen 2](https://murf.ai/api/docs/text-to-speech-models/gen-2) and [Synthesize](https://murf.ai/api/docs/text-to-speech/synthesize).
- **Model-specific voice catalogs:** Fetch streaming voices with `get_voices(model="falcon-2.1")` and studio voices with `get_voices(model="gen2")`. See [List Voices](https://murf.ai/api/docs/api-reference/voices/get-voices) and the [Voice Library](https://murf.ai/api/docs/voices-styles/voice-library).
- **150+ voices across 35 languages** and 20+ speaking styles.

![Murf AI Languages](https://murf.ai/public-assets/home/Murf_Languages_21.jpg)

- **Voice customization:** Adjust pitch, rate, locale, and pronunciation. Styles, pauses, duration, and variation are available on Synthesize (Gen 2).
- **Multiple audio formats:** MP3, WAV, FLAC, PCM, and others, with configurable sample rates.
- **Sync and async clients:** Blocking calls with `Murf`, or non-blocking calls with `AsyncMurf`.


---

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API.

```python
import asyncio
from murf import AsyncMurf, MurfRegion

client = AsyncMurf(
    api_key="YOUR_API_KEY",
    region=MurfRegion.GLOBAL,
)


async def main() -> None:
    audio_stream = client.text_to_speech.stream(
        text="Hi, How are you doing today?",
        voice_id="Gordon",
        model="falcon-2.1",
        locale="en-US",
        sample_rate=24000,
        format="PCM",
    )
    async for chunk in audio_stream:
        if chunk:
            pass


asyncio.run(main())
```

---

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from murf.core.api_error import ApiError

try:
    client.text_to_speech.generate(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

---

## Advanced

### Retries

The SDK is instrumented with automatic retries with exponential backoff. A request will be retried as long
as the request is deemed retriable and the number of retry attempts has not grown larger than the configured
retry limit (default: 2).

A request is deemed retriable when any of the following HTTP status codes is returned:

- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500) (Internal Server Errors)

Use the `max_retries` request option to configure this behavior.

```python
client.text_to_speech.generate(..., request_options={
    "max_retries": 1
})
```

### Timeouts

The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.

```python

from murf import Murf

client = Murf(
    ...,
    timeout=20.0,
)


# Override timeout for a specific method
client.text_to_speech.generate(..., request_options={
    "timeout_in_seconds": 1
})
```

### Custom Client

You can override the `httpx` client to customize it for your use-case. Some common use-cases include support for proxies
and transports.
```python
import httpx
from murf import Murf

client = Murf(
    ...,
    httpx_client=httpx.Client(
        proxies="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

---

## Contributing

We welcome contributions to enhance the Murf Python SDK. Please note that this library is generated programmatically, so direct modifications may be overwritten. We suggest opening an issue first to discuss your ideas or improvements. Contributions to the documentation are especially appreciated! For any support queries email to support@murf.ai 

---

## License

Murf Python SDK is released under the [MIT License](LICENSE).

---
