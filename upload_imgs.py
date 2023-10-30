# Copyright 2023 gyunseo
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import cloudinary

# Import the cloudinary.api for managing assets
import cloudinary.api

# Import the cloudinary.uploader for uploading assets
import cloudinary.uploader

import os

from dotenv import load_dotenv

load_dotenv()
cloudinary.config(
    cloud_name="gyunseo-blog",
    api_key="873459198774858",
    api_secret=os.environ.get("CLOUDINARY_API_SECRET"),
    secure=True,
)

# get all image files path in the directory

topics = [_ for _ in os.listdir() if os.path.isdir(_)]
print(topics)
for topic in topics:
    os.chdir(topic)
    sub_dirs = [_ for _ in os.listdir() if os.path.isdir(_)]
    print(sub_dirs)
    for sub_dir in sub_dirs:
        os.chdir(sub_dir)
        file_names = os.listdir()
        img_file_names = [
            file_name
            for file_name in file_names
            if file_name.endswith(".jpg") or file_name.endswith(".png")
        ]
        print(img_file_names)
        for img_file_name in img_file_names:
            print(img_file_name)
            response = cloudinary.uploader.upload(
                img_file_name,
                public_id=img_file_name.split(".")[0],
                tags=["algorithms", topic, "overwrite-test"],
                overwrite=False,
            )
            print(response)
        os.chdir("..")
    os.chdir("..")
