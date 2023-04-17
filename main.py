from datasets import Dataset, Audio


def main():
    # Create wav dataset
    audio_dataset_wav = Dataset.from_dict({"audio": ["audio_samples/audio.wav"]}).cast_column("audio", Audio())
    audio_dataset_wav.save_to_disk("audio_dataset_wav")

    # Create amr dataset
    audio_dataset_amr = Dataset.from_dict({"audio": ["audio_samples/audio.amr"]}).cast_column("audio", Audio())
    audio_dataset_amr.save_to_disk("audio_dataset_amr")

    # Read both datasets dataset
    audio_dataset_wav = Dataset.load_from_disk("audio_dataset_wav")
    audio_dataset_amr = Dataset.load_from_disk("audio_dataset_amr")

    print(audio_dataset_wav[0])
    print(audio_dataset_amr[0])


if __name__ == "__main__":
    main()
