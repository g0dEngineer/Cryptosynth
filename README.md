# Cryptosynth
A Cryptosynth Aeon (created by God Bennett/Cryptosynth Labs) is an artificial intelligence powered, artistically realistic 3d being, that anyone can actually hold a conversation with.

A Cryptosynth Aeon is an Ai powered NFT (Non-fungible-token) or Crypto-art that users can actually download and talk to, powered by blender3d and gpt-2 conversational ai module.


![Alt text](https://github.com/g0dEngineer/Cryptosynth/blob/main/BANNER.png "default page")

# Why open source cryptosynth?
To help collaboratively improve cyptosynths, I've decided to open source it here.

# Open-source versus synths that have already been Purchased
While the open source version has a sample ai generated cryptosynth aeon being, the open source does not have directions on how to create new synths, going from ai generated pictures to 3d model, which is available in purchased version.

# Contact
cryptosynthlabs@gmail.com

godquestbennett@gmail.com

facebook.com/God.Engineer

instagram.com/god_bennett

See [my prior github page](https://github.com/JordanMicahBennett/), that has my old name prior to [my legal name change to God](https://www.facebook.com/Cryptosynth/posts/114568167399002).

# Recommended Computer Specifications
Windows, GTX 1060+, i7 6700 CPU, 16 GB RAM. (8GB IS OKAY)

# Copyright
Copyright CryptosynthLabs 2021. Please don't redistribute without an arrangement with Cryptosynth Labs.

# A fun note
Each synth has a variety of genderless characters.

# Technical Summary

Essentially, each Cryptosynth Aeon being is a blender3d scene, integrated with pytorch based huggingface gpt2 conversational Ai agent. The solution is essentially a bledner3d file I wrote from scratch, combined with blender3d compatible conversational hugging face gpt2 ai. In fact, the plugin zip file I organized, includes my cryptosynth __ init __.py file, as well as the gpt2 hugging face ai library, where all hugging face ai files have been modified in order to be imported into my cryptosynth __ init __ controller file, which is about 225 lines of python code for interacting with Blender3d. 
	
![Alt text](https://github.com/g0dEngineer/Cryptosynth/blob/main/Cryptosynth_Core_Controller_Init_Py_Snippet.png?raw=true "default page")


# Quick Overview for general/partly technical understanding
Each Cryptosynth Aeon is an artificial intelligence powered, artistically realistic 3d being, that anyone can actually hold a conversation with, built in essentially 4 parts:

A: From scratch by God Bennett, a blender3d controller is made to enable the actions that the Cryotosynth Aeon 3d being performs. 
	See: __ init __.py in repository, which is the controller mentioned above.

B: Conversational artificial intelligence, which powers the cryptosynth aeon's ability to respond to user messages. (Built on top of huggingfaceai tech, converted into blender3d by God Bennett/Cryptosynth founder. Modification also includes crucial time complexity reduction, by removing personality randomization/dataset loading, which froze Blender3d Ui. This is replaced with single personalities per load; reducing load time from ~4 min to 5 seconds.)
	See: interact_cryptosynth.py in CRYPTOSYNTH_BLENDER_PLUGIN_AEON_sample_scene.zip plugin.


C: Blender3d model/scene enabling user to converse with 3d being. (Written from scratch by God Bennett/Cryptosynth founder)
	See: cryptosynth_sample_scene.blend file (In the cryptosynth_ sample_scene.zip file).

	
D: (A) and (B) are combined into a Blender3d plugin by God Bennett, for the purpose of easy loading into Blender3d by other users without the need for programming skills.



![Alt text](https://github.com/g0dEngineer/Cryptosynth/blob/main/0000.png "default page")

Quick snapshot of the [1st cryptosynth aeon being sold on Opensea](https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/62053288876263433244954069759722165048025551534616443775823876570185713319937).

# How to use:

## A-Auto setup textures: Auto-apply all aeon textures to 3d model, by :
1. Going to File > External Data > Find Missing Files 
2. Repeatedly press "Find Missing Files" until folder  model.fbm is found. (sample_scene_cryptosynth_blender\models\sample_scene\model.fbm\)
3. When in final folder with textres, press "Find Missing Files" once more, and witness textures being automatically applied.
4. Now that your model has textures, if the source, logo textures and code snippet picture to the right of your model are missing, do steps (1) to (3), stopping at the "sample_scene_cryptosynth_blender" directory before pressing "Find Missing Files".


## B-Talk to Aeon!!!

1. "I" key : *Initialize* Cryptosynth Aeon being. (Expand resulting dialog/popup (bottom left) with words "Aeon Initialization done")
2. Right click anywhere in 3d scene (like beside the synth) to enable Cryptosynth Aeon Dialog (bottom left screen).
3. "T" key : Start Aeon *thinking*/reading cycle. 
4. "R" key : Get *response* from Aeon being.







# Installation

## Part A - 3d Program and Cryptosynth assets setup

1. Download and install blender 2.91 (a popular 3d modeling program): 
https://www.blender.org/download/releases/2-91/

2. Download and extract the [sample Cryptosynth Blender 3d scene file](https://drive.google.com/file/d/1gYZUaboxTSwhIenVQKDgkirmlvvuUaVS/view?usp=sharing), which contains the 3d Aeon being and scene.

3. Open Blender3d 2.9, and then from File menu (top left) select open option then navigate to item from (2) above. 

You should see a scene with an untextured aeon being. Completing Part (B) and (C) below, and then following Instructions automatically gets your Aeon being ready for interaction and use.


## Part B - Python Setup

1. Download and install python 3.7:
https://www.python.org/downloads/release/python-370/

2. Download and extract [Cryptosynth Conversational Ai Windows Module](https://drive.google.com/file/d/1h7Iqlv5wSopniCh9166khBOQqQVKGD5H/view?usp=sharing). 
Fun note: Cryptosynth needs both the zip above as well as the plugin to work. However, the zip above is needed to generate the Ai brain which is explained below. This is closer to the original hugging face gpt2 code base, and lacks all modifications seen in the plugin format of the code, as this plugin is actually a further modified version of this code base, the biggest exception being my __ init __.py file explained in the [quick overview section](https://github.com/g0dEngineer/Cryptosynth#quick-overview-for-generalpartly-technical-understanding.

3. Specifically from Python37 scope, install all requirements in (2) immediately above.
	a. Open cmd. (Windows+r "cmd")
	b. In cmd (a), set path to python 37 path. (Eg type "path=C:\Users\18765\AppData\Local\Programs\Python\Python37" without quotes and hit enter.)
	c. In cmd (a), navigate to "Cryptosynth Conversational Ai Windows Module" folder from your downloaded of (2).
	d. In cmd (a), type command "python -m pip install -r requirements.txt" without quotes and hit enter, and wait till message at end indicating successful installation of modules from requirements.txt.

4. Test if (3) installed properly, by running the .bat file already provided in "LAUNCH_INTERACTION_py37.bat". 
You should see an Ai response talking about "My name is.." or "I am ..." or something similar. 
This is a quick test of the Conversational Ai module, where the ai is asked what its name is in the interact_cryptosynth.py file which the bat file calls.

4.b. Note the "tempdir" value, and save this directory in a text file somewhere. This is Aeon's brain!

6. On a windows folder, navigate to path from 3.b. (eg C:\Users\18765\AppData\Local\Programs\Python\Python37)

	5.b. Go to Lib\site-packages folder, and copy everything in that folder. (CTRL + A) then (CTRL + C).

7. Go to blender 2.91 python directory. (Eg: C:\Program Files\Blender Foundation\Blender 2.91)

	6.b. Go further into directory: 2.91\python\lib\site-packages. Hit (CTRL + P) to paste all content copied from path (5).


8. This concludes integration of python 37 Ai conversational module, into Blender3d. 

Fun-note: If you look closely, the plugin (from Part A/2) contains similar code to the Ai module (from Part C/1), which some differences:
	a. The Plugin (Part A/2) contains an extra file, called __init__.py; a file that controls 3d model's behaviour, and integrates ai response capbility into blender3d.
	b. The Plugin (Part A/2) imports things differently from the Windows module (Part C/1) 

	
	

## Part C - Cryptosynth Aeon plugin download & pointing plugin to Aeon's brain file

1. Download cryptosynth plugin utils.py, and edit file by changing tempdir value (under "download_pretrained_model") to directory of the result from 4.b. Ensure slashes in path face this "/" way:
https://bit.ly/3cBXrAE

2. Download ["Cryptosynth Aeon Communicate" plugin zip](https://drive.google.com/file/d/1caTu2UTFpFVMt-uzFvI2I-fw-hvZgUT4/view?usp=sharing) to for blender 2.91. At no point is an unzip required.
(All Cryptosynth plugins are custom for blender 2.91, and each plugin per aeon is again personalized to each Aeon)

3. Open (2) zip with Winrar, navigate to first place where you can see files, and just drag utils.py to the zip directory Cryptosynth Aeon Communicate from (2) immediately above. Agree to override if prompted. If not prompted, replace should still have been successful. This replaces utils.py in plugin, with the utils.py instance containing the directory to the ai brain. Don't unzip, as plugin will be added with new updated zip format to blender. (ENSURE YOU DROP utils.py in the same place you see the existing utils.py in the zip file)

Check zip file, by looking at utils.py (extract it to edit with notepad) to see if value in tempdir has changed to your value from Part B/4b.

4. Open Blender 3d 2.9. Go to Edit > Preferences > Install Then navigate to zip from (3) above. Select check to enable Cryptosynth Aeon plugin.

5. Click anywhere in 3d scene (like beside Aeon) and hit "Ctrl + alt + space" to maximize screen.

6. Blender3d now has the Cryptosynth addon (you can right click anywhere and see Cryptosynth.... in the Object Context Menu in blender3d), so Blender itself is now configured for execution of the addon, given that all prior Parts are done.

This adds the crucial user interface and ai integration into Blender3d, wrt Cryptosynth being.






# How is each Cryptosynth Aeon being is built?
https://www.facebook.com/Cryptosynth/posts/108859584636527

![Alt text](https://github.com/g0dEngineer/Cryptosynth/blob/main/How%20a%20cryptosynth%20aeon%20being%20created.png "default page")

1. An image of a completely fake, but realistic looking human is made using stylegan based GAN neural network
2. That photorealistic fake person is then converted to a 3d model in some program B.
3. An artificial intelligence brain, namely based on GPT-2, is personalized to the synth's theme.
4. A plugin was made for user interface into some program C; blender 2.91, which is carefully organized to render the 3d model (2) together with integration of the personalized ai brain (3), which any human user can interact with.
