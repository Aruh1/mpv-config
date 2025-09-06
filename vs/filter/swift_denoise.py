from vsdenoise import nl_means
from vsrgtools import contrasharpening

den = nl_means(video_in, h=1.25, planes=0)  # type:ignore
csharp = contrasharpening(den, video_in)  # type:ignore

csharp.set_output()
