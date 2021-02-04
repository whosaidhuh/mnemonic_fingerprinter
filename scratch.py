def trim_audio_files(mypath: str, label: str, t0: float, t1: float):
    """
    Trims mp3 file using seconds
    :param:
    :return:
    :example:
    :TODO: logging. at least one test. any([label in fn for fn in filenames])
    """
    from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
    from os import walk
    import logging
    logging.info('Starting')
    _, _, filenames = next(walk(mypath))
    if False:
        filenames = [f'{mypath}{f}' for f in filenames]
        for myfile in filenames:
            output = f'{myfile[:-4]}{label}{myfile[-4:]}'
            ffmpeg_extract_subclip(myfile, t0, t1, targetname=output)
    else:
        logging.info(f'The label({label}) already exists!')

    logging.info(f'Congratulations, there might be {label}s!')


def text2piano(text: str):
    """
    Converts text string to piano sounds.
    # text to metaphones
    # metaphone to piano key
    # generate piano key sequence
    # write piano key sequence as mp3
    # find audio files for piano keys in fingerprint
    # concatenate audio files into one file
    :param text:
    :return: mp3 file
    :example:
    :TODO: at least one test. add rests.
    """
    import phonetics
    import logging
    from pydub import AudioSegment
    _notes = ['A2', 'A3', 'A4', 'C1',
              'C2', 'C3', 'C4', 'C5', 'C6', 'Ds1', 'Ds2',
              'Ds3', 'Ds4', 'Fs2', 'Fs3', 'Fs4']
    _metaphones = list('0BFHJKLMNPRSTWXY')
    _meta2piano = dict(zip(_metaphones, _notes))
    metaphones = list(phonetics.metaphone(text))
    fingerprint = [_meta2piano[phone] for phone in metaphones]
    filenames = [f'{mypath}{f}_quart.mp3' for f in fingerprint]

    _mp3s = [AudioSegment.from_mp3(file) for file in filenames]
    _mp3 = sum(_mp3s)
    _outputmp3 = f"{mypath}{text}{''.join(metaphones)}.mp3".replace(' ','')
    logging.info(_outputmp3)
    print(text)
    print(_outputmp3)
    _mp3.export(_outputmp3, format="mp3")


if __name__ == '__main__':
    t0, t1 = 0, .25
    label = '_quart'
    text = "mnemonic fingerprint"
    mypath = '/home/a/projects/mnemonic_fingerprinter/assets/audio/'
    trim_audio_files(mypath, label, t0, t1)
    text2piano(text)
