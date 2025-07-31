import os
from PIL import Image 
from PIL import ImageEnhance


root_dir="resized_fabrics_images_pillow"

for root,dir,files in os.walk(root_dir):
    for file in files:
        if file.lower().endswith(".jpg"):
            full_path_image_resize=os.path.join(root,file)
            
            try:
                img_resized=Image.open(full_path_image_resize)
                img_resized=img_resized.convert("RGB")
                
                relative_path = os.path.relpath(root, root_dir)
                subfolder_name = relative_path.lower().replace(" ", "_")
                save_dir = os.path.join("augmented_fabrics_images_pillow", subfolder_name)
                os.makedirs(save_dir, exist_ok=True)

                base_filename = os.path.splitext(file)[0]
                
                # horizontal flip
                flipped_img_resized=img_resized.transpose(Image.FLIP_LEFT_RIGHT)
                flipped_img_resized.save(os.path.join(save_dir,base_filename + "_flip.jpg"))
                
                
                # rotation
                
                rotated_img_resized=img_resized.rotate(-20,expand=True)
                rotated_img_resized.save(os.path.join(save_dir,base_filename + "_rotated.jpg"))
                
                
                # brightness ajustment 
                
                bright_img_resized=ImageEnhance.Brightness(img_resized).enhance(1.5)
                bright_img_resized.save(os.path.join(save_dir,base_filename + "_brigth.jpg"))
                
                print(f" Augmented and saved in : {file}")

            except Exception as aug_e:
                    print(f" Failed to augment {file}: {aug_e}")
                
                
                
            
            
            
            
            
            
    