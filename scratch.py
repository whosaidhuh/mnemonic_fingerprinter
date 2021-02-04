def trim_audio_files():
    """
    Trims mp3 file using seconds
    :param:
    :return:
    :example:
    """
    from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
    from os import walk

    mypath = '/home/a/projects/mnemonic_fingerprinter/assets/audio/'
    _, _, filenames = next(walk(mypath))
    filenames = [f'{mypath}{f}' for f in filenames]
    for myfile in filenames:
        output = f'{myfile[:-4]}_half{myfile[-4:]}'
        ffmpeg_extract_subclip(myfile, 0, .5, targetname=output)


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
    :TODO:
    """
    import phonetics
    from os import walk
    _notes = ['A2', 'A3', 'A4', 'C1',
              'C2', 'C3', 'C4', 'C5', 'C6', 'Ds1', 'Ds2',
              'Ds3', 'Ds4', 'Fs2', 'Fs3', 'Fs4']
    _metaphones = list('0BFHJKLMNPRSTWXY')
    _meta2piano = dict(zip(_metaphones, _notes))
    text = "mnemonic fingerprint"
    metaphones = list(phonetics.metaphone(text))
    fingerprint = [_meta2piano[phone] for phone in metaphones]

    mypath = '/home/a/projects/mnemonic_fingerprinter/assets/audio/'
    _, _, filenames = next(walk(mypath))
    filenames = [f'{mypath}{f}' for f in filenames]
    print(filenames)





if __name__ == '__main__':
    trim_audio_files()
