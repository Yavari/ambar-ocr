Docker container to OCR images and pdf files. 

The code has been taken from  https://github.com/RD17/ambar 

Build

    docker build -t ocr .

Run

    docker run --rm --volume path:/var ocr //var/file.png //var/out.txt