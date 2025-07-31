import os
from PIL import Image 
from PIL import ImageOps

root_dir_main_file= "Fabrics_image"

for root,dir,files in os.walk(root_dir_main_file):
    for file in files:
        if file.lower().endswith(".jpg"):
            full_path_images=os.path.join(root,file)
            
            try:
                img_fabrics=Image.open(full_path_images)
                img_fabrics=img_fabrics.convert("RGB")
                
                width,height=img_fabrics.size
                    
                if width!=height:
                    
                    if width>height:
                        diff_1=width-height
                        
                        pad_top=diff_1//2
                        pad_bottom=diff_1-pad_top
                        img_fabrics=ImageOps.expand(img_fabrics,border=(0,pad_top,0,pad_bottom),fill=(255,255,255))
                    
                    else:
                        diff_2=height-width    
                            
                        pad_left=diff_2//2
                        pad_right=diff_2-pad_left
                        img_fabrics=ImageOps.expand(img_fabrics,border=(pad_left,0,pad_right,0),fill=(255,255,255))
                            
                            
                new_size=(224,224)
                        
                img_fabrics=img_fabrics.resize(new_size)
                            
                
                
                relative_path = os.path.relpath(root, root_dir_main_file)
                subfolder_name = relative_path.lower().replace(" ", "_")

                
                save_dir = os.path.join("resized_fabrics_images", subfolder_name)
                os.makedirs(save_dir, exist_ok=True)

                # Save processed image
                save_path = os.path.join(save_dir, file)
                img_fabrics.save(save_path)

                print(f" Saved: {save_path}")

            except Exception as e:
                print(f" Failed to process {full_path_images}: {e}")
                     
                