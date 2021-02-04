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


if __name__ == '__main__':
    trim_audio_files()