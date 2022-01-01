Author: God Quest Bennett/Cryptosynth Labs

Title: God's instructions/guide for configuring [stylegan 2](https://github.com/NVlabs/stylegan2/) on windows, for generating starting images of artificial people like the 2d images that were used to construct [my 3d cryptosynths](https://github.com/g0dEngineer/Cryptosynth), which can also be used to generate cars, houses, etc. 

* Each intelligent cryptosynhs are constructed starting with fake images of realistic looking humans, using stylegan2.

* These now publicly released instructions were priorly provided [with each synth sold on opensea](https://opensea.io/collection/cryptosynth/), ..since [its inception](https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/62053288876263433244954069759722165048025551534616443775823876570185713319937)... (to allow for creation of custom synths), beyond the open source synth sample guide.

* After the stylegan 2 samples are generated, they form inputs to a 3d program (program B) which auto-converts the image to 3d face, after which I integrated gpt-2 into blender (program C) while rendering the 3d face in the configuratio seen in the crypsotynth open source.

* I also used this process [in my rarible cars](https://rarible.com/token/0x60f80121c31a0d46b5279700f9df786054aa5ee5:325535?tab=details) are not real series.

![image](https://github.com/g0dEngineer/Cryptosynth/blob/main/readme_images/0000.png)

Requirements: Windows Desktop or laptop with at least GTX 1060 gpu.

Bonus: I will guide your through the unlocked instructions(18 steps) + source code, if desired.


1. Download and install python 3.6.

2. Download stylegan 2 python project: -> https://github.com/justinpinkney/stylegan2

3. Update graphics drivers. (Any applicable nvidia gpu driver)

4. Install Cuda 10.

5. Download cuDNN v7.5  for CUDA 10.0.

6. Install visual studio 2017 commnunity.

7. Install visual studio 14 if not already installed. Something like "C:\Program Files (x86)\Microsoft Visual Studio 14.0" should exist after install.

8. After doing 2017 commnunity run install again, and modify 2017 commnunity to include (a few gigs):
	i. Windows Universal CRT SDK
	ii. Windows 10 SDK 
	iii. VC++ 2015.3 v14.00 toolset for tesktop

9. Ensure environement variable is setup to include items similar to the following:
	C:\Users\18765\AppData\Local\Programs\Python\Python36
	C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin
	C:\Program Files (x86)\Windows Kits\10\Include\10.0.10240.0\ucrt
	C:\Users\18765\Downloads\cudnn-10.0-windows10-x64-v7.5.0.56\cuda\bin
	C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\bin
	C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\libnvvp

10. Modify lib/include in environment variables:
	INCLUDE:
	C:\Program Files (x86)\Windows Kits\10\Lib\10.0.10240.0\ucrt

	LIB
	C:\Program Files (x86)\Windows Kits\10\Lib\10.0.10240.0\um\x64
	C:\Program Files (x86)\Windows Kits\10\Lib\10.0.10240.0\ucrt\x64
		
		
11. Install tensorflow-gpu 1.14.0.
	Note if you get dlib build red line errors, you need to:
		Install cmake 3.19.4, and visual studio build tools. (this build tools is different from the items prior)
		After installing build tools.
	
12. Ensure tensorflow is not installed. Ensure only tensorflow-gpu==1.14.0 is installed.

13. Restart computer. Tensorflow may not detect GPU until restart.

14. Navigate to cuda 10 bin. Right click on cudafe++.exe, and enable run as administrator , to avoid "nvcc error : 'cudafe++' died with status 0xC0000005 (ACCESS_VIOLATION)" error. God Bennett (myself) came up with this quick solution, instead of the CUDA 10.1 download workaround solution proposed online, which is 2 gb download.
	Example location: C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\bin

	
15. Download at least 1 car stylegan model from https://drive.google.com/drive/folders/1yanUI9m4b4PWzR0eurKNq6JR1Bbfbh6L. 
This is the same as models provided by NVIDIA/stylegan2. Can be any one from "stylegan2-car-config-a.pkl" to "stylegan2-car-config-f.pkl".


16. We will not use the the grid_vid.py latent walk generator from justinpinkney/stylegan2, which leads to an Operand error at execution on the pretrained model.


a) Instead, download lzhbrian's copy of "gen_video_interpolation.py" from https://gist.github.com/lzhbrian/75dd7e58444c4469b4b341d36b0cc09b#file-gen_video_interpolation-py.

b) Make the necessary changes, to load any of the "stylegan2-car...pkl" networks, by changing fpath variable.

Example fpath = 'C:/Backup/Downloads/God/RobotizeJA/crypto/ai_generated_cars/stylegan2-master_pin/stylegan2-car-config-f.pkl'

c) Make sure to specify output file name, where resulting video will be stored, by modifying mp4 parameter in generate_interpolation_video function.

Example  mp4='C:/Backup/Downloads/God/RobotizeJA/crypto/ai_generated_cars/stylegan2-master_pin/output.mp4'

d) You can also modify other parameters there, like video duration.

17. Get ffmpeg in python idle:
	import imageio
	imageio.plugins.ffmpeg.download()

18. Run interpolation python script: Example -> python C:/Backup/Downloads/God/RobotizeJA/crypto/cryptosynth/00_cryptosynth_appearance_gen/run_generator.py generate-images --network=stylegan2-ffhq-config-d.pkl --seeds=0-25 --truncation-psi=0.5


