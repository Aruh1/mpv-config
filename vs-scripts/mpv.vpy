from vapoursynth import core

clip = video_in

clip = core.ffms2.Source(clip)
clip.set_output()