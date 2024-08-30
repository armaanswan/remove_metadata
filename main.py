import ffmpeg

input_file = 'input.txt'
output_file = 'output.txt'

ffmpeg.input(input_file).output(output_file, map_metadata='-1').run()