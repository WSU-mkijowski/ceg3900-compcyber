# Example notes


### Meta:

Downloading files:

* if you have a web URL to a given file you can download that file with `wget "<URL>"`
  * for exmaple: `wget "https://assets.super.so/2bd352bd-0121-4de9-82cb-b0261b7e35e9/images/1d526754-16a7-4582-9414-fb031dfbca4a/Meta_(6).jpg"`
  * note the quotes needed to escape the special `()` characters.

* I had the best luck with `imagemagick` which when installed provides a `identify <filename.jpg>` command
  * when used with the `-verbose` flag I was able top extract the image metadata

```bash
mkijowski@minibop:~$ identify ./Meta_\(6\).jpg
./Meta_(6).jpg JPEG 1024x768 1024x768+0+0 8-bit sRGB 68788B 0.000u 0:00.001
mkijowski@minibop:~$ identify -verbose ./Meta_\(6\).jpg
Image:
  Filename: ./Meta_(6).jpg
  Permissions: rw-r--r--
  Format: JPEG (Joint Photographic Experts Group JFIF format)
  Mime type: image/jpeg
  Class: DirectClass
  Geometry: 1024x768+0+0
  Units: Undefined
  Colorspace: sRGB
  Type: TrueColor
  Base type: Undefined
  Endianness: Undefined
  Depth: 8-bit
  Channels: 3.0
  Channel depth:
    Red: 8-bit
    Green: 8-bit
    Blue: 8-bit
  Channel statistics:
    Pixels: 786432
    Red:
      min: 0  (0)
      max: 255 (1)
      mean: 84.6518 (0.331968)
      median: 61 (0.239216)
      standard deviation: 64.7222 (0.253812)
      kurtosis: -0.133848
      skewness: 1.07439
      entropy: 0.930393
    Green:
      min: 0  (0)
      max: 255 (1)
      mean: 91.4823 (0.358754)
      median: 75 (0.294118)
      standard deviation: 59.3714 (0.232829)
      kurtosis: -0.0787867
      skewness: 0.939121
      entropy: 0.94906
    Blue:
      min: 0  (0)
      max: 255 (1)
      mean: 52.8655 (0.207316)
      median: 15 (0.0588235)
      standard deviation: 71.8678 (0.281835)
      kurtosis: 0.334054
      skewness: 1.37716
      entropy: 0.812653
  Image statistics:
    Overall:
      min: 0  (0)
      max: 255 (1)
      mean: 76.3332 (0.299346)
      median: 50.3333 (0.197386)
      standard deviation: 65.3205 (0.256159)
      kurtosis: 0.0404732
      skewness: 1.13023
      entropy: 0.897369
  Rendering intent: Perceptual
  Gamma: 0.454545
  Chromaticity:
    red primary: (0.64,0.33,0.03)
    green primary: (0.3,0.6,0.1)
    blue primary: (0.15,0.06,0.79)
    white point: (0.3127,0.329,0.3583)
  Matte color: grey74
  Background color: white
  Border color: srgb(223,223,223)
  Transparent color: black
  Interlace: None
  Intensity: Undefined
  Compose: Over
  Page geometry: 1024x768+0+0
  Dispose: Undefined
  Iterations: 0
  Compression: JPEG
  Quality: 80
  Orientation: Undefined
  Properties:
    date:create: 2026-01-28T17:09:02+00:00
    date:modify: 2024-10-17T01:32:00+00:00
    date:timestamp: 2026-01-28T17:12:30+00:00
    jpeg:colorspace: 2
    jpeg:sampling-factor: 2x2,1x1,1x1
    signature: 36a77bf926fdee6141f8fda9bea6ef13e5534618441cf7d14c37e479bd957238
  Artifacts:
    verbose: true
  Tainted: False
  Filesize: 68788B
  Number pixels: 786432
  Pixel cache type: Memory
  Pixels per second: 17.9974MP
  User time: 0.010u
  Elapsed time: 0:01.043
  Version: ImageMagick 7.1.2-13 Q16-HDRI x86_64 2fae24192:20260118 https://imagemagick.org
```

I did the thing 
