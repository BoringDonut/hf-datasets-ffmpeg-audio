# write and read .amr files in HF Datasets

This repo showcases a situation where you can create a dataset with audio files that you can't read later without
falling back on ffmpeg.

The script should fail with the folowing error:
```
    raise LibsndfileError(err, prefix="Error opening {0!r}: ".format(self.name))
soundfile.LibsndfileError: Error opening <_io.BytesIO object at 0x7f316323e4d0>: Format not recognised.
```


## Usage

```
python main.py
```

## Notes
Files in [audio_samples](audio_samples) directory are derived from
[buzz roll.wav](https://freesound.org/people/bigjoedrummer/sounds/77305/)
sound from [freesound.org](https://freesound.org/).



