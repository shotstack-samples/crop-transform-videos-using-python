{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Render Successfully Queued\n",
      "\n",
      ">> render id: 1ef58271-2c6d-4b24-a5a4-87867d57141d\n"
     ]
    }
   ],
   "source": [
    "import shotstack_sdk as shotstack\n",
    "import os\n",
    "import sys\n",
    "\n",
    "from shotstack_sdk.api import edit_api\n",
    "from shotstack_sdk.model.clip import Clip\n",
    "from shotstack_sdk.model.track import Track\n",
    "from shotstack_sdk.model.timeline import Timeline\n",
    "from shotstack_sdk.model.output import Output\n",
    "from shotstack_sdk.model.edit import Edit\n",
    "from shotstack_sdk.model.video_asset import VideoAsset\n",
    "from shotstack_sdk.model.rotate_transformation import RotateTransformation\n",
    "from shotstack_sdk.model.skew_transformation import SkewTransformation\n",
    "from shotstack_sdk.model.flip_transformation import FlipTransformation\n",
    "from shotstack_sdk.model.transformation import Transformation\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    host = \"https://api.shotstack.io/stage\"\n",
    "\n",
    "    configuration = shotstack.Configuration(host = host)\n",
    "\n",
    "    configuration.api_key['DeveloperKey'] = os.getenv(\"SHOTSTACK_KEY\")\n",
    "    \n",
    "    with shotstack.ApiClient(configuration) as api_client:\n",
    "        api_instance = edit_api.EditApi(api_client)\n",
    "\n",
    "        video_asset = VideoAsset(\n",
    "        src = \"https://s3-ap-southeast-2.amazonaws.com/shotstack-assets/footage/skater.hd.mp4\"\n",
    "        )\n",
    "        \n",
    "        rotate = RotateTransformation(\n",
    "            angle = 180\n",
    "        )\n",
    "\n",
    "        skew = SkewTransformation(\n",
    "            x = 0.20\n",
    "        )\n",
    "\n",
    "        flip = FlipTransformation(\n",
    "            vertical = True\n",
    "        )\n",
    "\n",
    "        transformation = Transformation(\n",
    "            rotate  = rotate,\n",
    "            skew    = skew,\n",
    "            flip    = flip\n",
    "        )\n",
    "        \n",
    "        video_clip = Clip(\n",
    "            asset = video_asset,\n",
    "            start = 0.0,\n",
    "            length= 8.0,\n",
    "            transform = transformation\n",
    "        )\n",
    "    \n",
    "        track = Track(clips=[video_clip])\n",
    "\n",
    "        timeline = Timeline(\n",
    "            background = \"#000000\",\n",
    "            tracks     = [track]\n",
    "        )\n",
    "\n",
    "        output = Output(\n",
    "            format      = \"mp4\",\n",
    "            resolution  = \"sd\"\n",
    "        )\n",
    "\n",
    "        edit = Edit(\n",
    "            timeline = timeline,\n",
    "            output   = output\n",
    "        )\n",
    "\n",
    "        try:\n",
    "            api_response = api_instance.post_render(edit)\n",
    "\n",
    "            message = api_response['response']['message']\n",
    "            id = api_response['response']['id']\n",
    "        \n",
    "            print(f\"{message}\\n\")\n",
    "            print(f\">> render id: {id}\")\n",
    "        except Exception as e:\n",
    "            print(f\"Unable to resolve API call: {e}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.10.5 64-bit",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.5"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "320c2aa7335eeb14aab0f62951f10a1684c6fc87df598ed296cdfb09eda94d8c"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
