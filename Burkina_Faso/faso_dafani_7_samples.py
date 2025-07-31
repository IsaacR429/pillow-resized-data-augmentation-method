import pandas as pd 

metadata_faso_dan_fani = [
    {
        "image_filename": "faso_dan_fani_01.jpg",
        "fabric_name": "Faso Dan Fani",
        "country_of_origin": "Burkina Faso",
        "color_scheme": "White, Blue",
        "image_type": "Flat",
        "cultural_use": "Everyday wear",
        "notes": "Narrow horizontal stripes",
        "motif_type": "Stripes, Blocks",
        "material": "Cotton (handwoven)"
    },
    {
        "image_filename": "faso_dan_fani_02.jpg",
        "fabric_name": "Faso Dan Fani",
        "country_of_origin": "Burkina Faso",
        "color_scheme": "Purple, White",
        "image_type": "Flat",
        "cultural_use": "Ceremonial",
        "notes": "Woven by hand in Bobo-Dioulasso",
        "motif_type": "Stripes, Blocks",
        "material": "Cotton (handwoven)"
    },
    {
        "image_filename": "faso_dan_fani_03.jpg",
        "fabric_name": "Faso Dan Fani",
        "country_of_origin": "Burkina Faso",
        "color_scheme": "Black, Teal, White",
        "image_type": "Close-up",
        "cultural_use": "Ceremonial",
        "notes": "Variant with border motif",
        "motif_type": "Stripes, Blocks",
        "material": "Cotton (handwoven)"
    },
    {
        "image_filename": "faso_dan_fani_04.jpg",
        "fabric_name": "Faso Dan Fani",
        "country_of_origin": "Burkina Faso",
        "color_scheme": "Yellow, Black",
        "image_type": "Worn",
        "cultural_use": "Traditional",
        "notes": "Male outfit for national event",
        "motif_type": "Stripes, Blocks",
        "material": "Cotton (handwoven)"
    },
    {
        "image_filename": "faso_dan_fani_05.jpg",
        "fabric_name": "Faso Dan Fani",
        "country_of_origin": "Burkina Faso",
        "color_scheme": "Red, Green",
        "image_type": "Worn",
        "cultural_use": "Ceremonial",
        "notes": "Worn at Bobo Week fashion show",
        "motif_type": "Stripes, Blocks",
        "material": "Cotton (handwoven)"
    },
    {
        "image_filename": "faso_dan_fani_06.jpg",
        "fabric_name": "Faso Dan Fani",
        "country_of_origin": "Burkina Faso",
        "color_scheme": "Pink, Black",
        "image_type": "Worn",
        "cultural_use": "Modern fashion",
        "notes": "Fusion design with vertical lines",
        "motif_type": "Stripes, Blocks",
        "material": "Cotton (handwoven)"
    },
    {
        "image_filename": "faso_dan_fani_07.jpg",
        "fabric_name": "Faso Dan Fani",
        "country_of_origin": "Burkina Faso",
        "color_scheme": "Blue, White",
        "image_type": "Flat",
        "cultural_use": "Formal",
        "notes": "Symmetrical stripe pattern",
        "motif_type": "Stripes, Blocks",
        "material": "Cotton (handwoven)"
    },
    {
    "image_filename": "faso_dafani_sample_8.jpg",
    "fabric_name": "Faso Dan Fani",
    "country_of_origin": "Burkina Faso",
    "color_scheme": "Red, Gold",
    "image_type": "Worn",
    "cultural_use": "Ceremonial, Traditional Leadership",
    "notes": "Rich embroidery, worn with cap and staff",
    "motif_type": "Vertical stripes, Embroidery",
    "material": "Cotton (handwoven)"
    },
    {
    "image_filename": "faso_dafani_sample_9.jpg",
    "fabric_name": "Faso Dan Fani",
    "country_of_origin": "Burkina Faso",
    "color_scheme": "White, Blue",
    "image_type": "Worn",
    "cultural_use": "Modern casual wear",
    "notes": "Minimal embroidery, bright background",
    "motif_type": "Vertical stripes",
    "material": "Cotton (handwoven)"
    },
    {
    "image_filename": "faso_dafani_sample_10.jpg",
    "fabric_name": "Faso Dan Fani",
    "country_of_origin": "Burkina Faso",
    "color_scheme": "Green, Orange, Beige",
    "image_type": "Worn",
    "cultural_use": "Ceremonial (weddings, engagement)",
    "notes": "Worn with head wrap and traditional beads",
    "motif_type": "Diagonal stripes",
    "material": "Cotton blend"
    },
    {
    "image_filename": "faso_dafani_sample_11.jpg",
    "fabric_name": "Faso Dan Fani",
    "country_of_origin": "Burkina Faso",
    "color_scheme": "Black, Yellow",
    "image_type": "Worn",
    "cultural_use": "Ceremonial or prestige events",
    "notes": "Bold vertical gold patterns, agbada style",
    "motif_type": "Vertical stripes, Embroidery",
    "material": "Cotton (handwoven)"
    },
    {
    "image_filename": "faso_dafani_sample_12.jpg",
    "fabric_name": "Faso Dan Fani",
    "country_of_origin": "Burkina Faso",
    "color_scheme": "White, Yellow, Black",
    "image_type": "Flat",
    "cultural_use": "Everyday wear and tailoring",
    "notes": "Presented laid flat, folded sleeves",
    "motif_type": "Narrow vertical stripes",
    "material": "Cotton (handwoven)"
    },
    {
    "image_filename": "faso_dafani_sample_13.jpg",
    "fabric_name": "Faso Dan Fani",
    "country_of_origin": "Burkina Faso",
    "color_scheme": "White, Yellow, Green, Blue",
    "image_type": "Worn",
    "cultural_use": "Modern interpretation of traditional attire",
    "notes": "Photographed on green background",
    "motif_type": "Multicolor vertical stripes",
    "material": "Cotton (handwoven)"
    },
    {
    "image_filename": "faso_dafani_sample_14.jpg",
    "fabric_name": "Faso Dan Fani",
    "country_of_origin": "Burkina Faso",
    "color_scheme": "Blue, Black, White",
    "image_type": "Worn",
    "cultural_use": "Formal events",
    "notes": "Model wearing traditional dress and beads",
    "motif_type": "Stripes",
    "material": "Cotton blend"
    },
    {
    "image_filename": "faso_dafani_sample_15.jpg",
    "fabric_name": "Faso Dan Fani",
    "country_of_origin": "Burkina Faso",
    "color_scheme": "Black, Purple, White",
    "image_type": "Flat",
    "cultural_use": "Tailoring / Cloth sales",
    "notes": "Rolled and laid fabric view",
    "motif_type": "Horizontal and vertical stripes",
    "material": "Cotton (handwoven)"
    },
    {
    "image_filename": "faso_dafani_sample_16.jpg",
    "fabric_name": "Faso Dan Fani",
    "country_of_origin": "Burkina Faso",
    "color_scheme": "Blue, White",
    "image_type": "Flat",
    "cultural_use": "Tailoring / Cloth sales",
    "notes": "Rolled and laid diagonally",
    "motif_type": "Diagonal lines",
    "material": "Cotton (handwoven)"
    },
    {
    "image_filename": "faso_dafani_sample_17.jpg",
    "fabric_name": "Faso Dan Fani",
    "country_of_origin": "Burkina Faso",
    "color_scheme": "Black, Yellow, Red, White",
    "image_type": "Flat",
    "cultural_use": "Festive wear",
    "notes": "Warm color palette, dynamic stripe thickness",
    "motif_type": "Stripes",
    "material": "Cotton (handwoven)"
    },
    {
    "image_filename": "faso_dafani_sample_18.jpg",
    "fabric_name": "Faso Dan Fani",
    "country_of_origin": "Burkina Faso",
    "color_scheme": "White, Yellow, Black",
    "image_type": "Flat",
    "cultural_use": "Formal",
    "notes": "Elegant composition with horizontal woven details",
    "motif_type": "Stripes",
    "material": "Cotton (handwoven)"
    }


    





   



]


df = pd.DataFrame(metadata_faso_dan_fani)


df.to_csv("faso_dan_fani_metadata.csv", index=False)
