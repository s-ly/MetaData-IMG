from exif import Image


while True:


    file_name = input('\nИмя файла: ')


    # чтение файла
    with open(file_name, "rb") as img_file:
        img = Image(img_file)


    if img.has_exif:        
        status = f"contains EXIF (version {img.exif_version}) information."
        print(f"Image {status}")

        print(img.model)
        print(img.datetime)
    else:
        status = "does not contain any EXIF information."
        print(f"Image {status}")

    # img_dir = dir(img)
    # for i in img_dir:
    #     print(i)

    # print('\n' + img.model)
    # print('\n' + img.datetime)
    # print('\n' + img.make)

    # image_members = []

    # for image in images:
    #     image_members.append(dir(image))

    # for index, image_member_list in enumerate(image_members):
    #     print(f"Image {index} contains {len(image_member_list)} members:")
    #     print(f"{image_member_list}\n")

