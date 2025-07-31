import pandas as pd

kancheepuram_metadata = [
    {
        "image_filename": "kancheepuram_silk_1.jpg",
        "fabric_name": "Kancheepuram Silk",
        "country_of_origin": "India",
        "color_scheme": "Black, Copper, Gold",
        "image_type": "Flat",
        "cultural_use": "Traditional ceremony",
        "notes": "Zari border with geometric floral motifs",
        "motif_type":"Floral zari vines on pallu, small butta on body, temple-style gold border",
        "material":"Pure silk body with copper zari border"
    },
    {
        "image_filename": "kancheepuram_silk_2.jpg",
        "fabric_name": "Kancheepuram Silk",
        "country_of_origin": "India",
        "color_scheme": "Green, Black, Gold",
        "image_type": "Flat",
        "cultural_use": "Festival wear",
        "notes": "Peacock motifs and rich temple border",
        "motif_type":"Paisley (mango) motifs along the border, diamond lattice body",
        "material":"Silk with traditional gold zari (Korvai weave)"
    },
    {
        "image_filename": "kancheepuram_silk_3.jpg",
        "fabric_name": "Kancheepuram Silk",
        "country_of_origin": "India",
        "color_scheme": "Purple, Red, Gold",
        "image_type": "Close-up",
        "cultural_use": "Wedding saree",
        "notes": "Floral round butta with temple border",
        "motif_type":"Circular chakra motifs and rich temple border",
        "material":"Handwoven silk with antique gold zari"
    },
    {
        "image_filename": "kancheepuram_silk_4.jpg",
        "fabric_name": "Kancheepuram Silk",
        "country_of_origin": "India",
        "color_scheme": "Yellow, Purple, Gold",
        "image_type": "Folded/Flat",
        "cultural_use": "Temple visit",
        "notes": "Modern zari lines with chakra border",
        "motif_type":"Vertical zari stripes with traditional flower-row motifs",
        "material":"Mulberry silk with contrast violet border and gold zari"
    },
    {
        "image_filename": "kancheepuram_silk_5.jpg",
        "fabric_name": "Kancheepuram Silk",
        "country_of_origin": "India",
        "color_scheme": "Orange, Green, Gold",
        "image_type": "Worn (Mannequin)",
        "cultural_use": "Formal event saree",
        "notes": "Contrast border with gold checkered motifs",
        "motif_type":"Wavy temple borders with embedded lotus motifs",
        "material":"Traditional silk with copper zari"
    },
    {
        "image_filename": "kancheepuram_silk_6.jpg",
        "fabric_name": "Kancheepuram Silk",
        "country_of_origin": "India",
        "color_scheme": "Beige, Brown, Black",
        "image_type": "Worn",
        "cultural_use": "Casual traditional attire",
        "notes": "Subtle color with elegant temple stripes",
        "motif_type":"Tribal temple borders, diagonal stripe weave",
        "material":"Lightweight silk with matte zari"
    },
    {
        "image_filename": "kancheepuram_silk_7.jpg",
        "fabric_name": "Kancheepuram Silk",
        "country_of_origin": "India",
        "color_scheme": "Lime Green, Purple, Gold",
        "image_type": "Worn",
        "cultural_use": "Cultural celebration",
        "notes": "Bright silk with bold zari border",
        "motif_type":"Temple tower (gopuram) design on border, floral band on pallu",
        "material":"Soft silk with luminous golden zari"
    },
    {
    "image_filename": "kancheepuram_silk_8.jpg",
    "fabric_name": "Kancheepuram Silk",
    "country_of_origin": "India",
    "color_scheme": "Green, Pink, Orange, Purple",
    "image_type": "Flat",
    "cultural_use": "Traditional wear",
    "notes": "Bold checked pattern with temple borders and vibrant color blocking",
    "motif_type": "Temple-style border, checked body",
    "material": "Silk with gold thread border"
    },
    {
    "image_filename": "kancheepuram_silk_9.jpg",
    "fabric_name": "Kancheepuram Silk",
    "country_of_origin": "India",
    "color_scheme": "Orange, Purple, Gold, Green",
    "image_type": "Worn",
    "cultural_use": "Wedding or festive attire",
    "notes": "Ornate traditional drape with temple border and zari detailing, accessorized with jewelry and backdrop idol",
    "motif_type": "Floral, Temple-style border, Ikat-inspired pallu",
    "material": "Pure silk with gold zari"
    },
    {
    "image_filename": "kancheepuram_silk_10.jpg",
    "fabric_name": "Kancheepuram Silk",
    "country_of_origin": "India",
    "color_scheme": "Purple, Gold",
    "image_type": "Flat",
    "cultural_use": "Formal ceremony or bridal wear",
    "notes": "Rich peacock and floral zari border on purple silk with fine detailing and sheen",
    "motif_type": "Peacock, Floral vines, Geometric grid",
    "material": "Pure silk with gold zari brocade"
    },
    {
    "image_filename": "kancheepuram_silk_11.jpg",
    "fabric_name": "Kancheepuram Silk",
    "country_of_origin": "India",
    "color_scheme": "Blue, Green, Gold",
    "image_type": "Flat Display",
    "cultural_use": "Cultural gatherings",
    "notes": "Bright blue and green checks with gold floral border",
    "motif_type": "Checks, Floral motifs",
    "material": "Silk with Zari"
  },
  {
    "image_filename": "kancheepuram_silk_12.jpg",
    "fabric_name": "Kancheepuram Silk",
    "country_of_origin": "India",
    "color_scheme": "Yellow, Green, Gold",
    "image_type": "Worn",
    "cultural_use": "Bharatanatyam costume",
    "notes": "Traditional temple dancer’s saree style",
    "motif_type": "Temple border, Gold stripe",
    "material": "Silk with Zari"
  },
  {
    "image_filename": "kancheepuram_silk_13.jpg",
    "fabric_name": "Kancheepuram Silk",
    "country_of_origin": "India",
    "color_scheme": "Black, Pink, Orange, Gold",
    "image_type": "Flat Display",
    "cultural_use": "Formal occasions",
    "notes": "Vibrant geometric patterns with dark base",
    "motif_type": "Zigzag, Checked",
    "material": "Silk with Zari"
  },
  {
    "image_filename": "kancheepuram_silk_14.jpg",
    "fabric_name": "Kancheepuram Silk",
    "country_of_origin": "India",
    "color_scheme": "Yellow, Green, Gold",
    "image_type": "Flat Display",
    "cultural_use": "Festive rituals",
    "notes": "Golden motifs on vibrant yellow base",
    "motif_type": "Floral brocade",
    "material": "Silk with Zari"
  },
  {
    "image_filename": "kancheepuram_silk_15.jpg",
    "fabric_name": "Kancheepuram Silk",
    "country_of_origin": "India",
    "color_scheme": "Yellow, Black, Red, Gold",
    "image_type": "Worn",
    "cultural_use": "Pooja and festivals",
    "notes": "Heavy border with traditional motifs",
    "motif_type": "Temple, Paisley, Brocade",
    "material": "Silk with Zari"
  },
  {
    "image_filename": "kancheepuram_silk_16.jpg",
    "fabric_name": "Kancheepuram Silk",
    "country_of_origin": "India",
    "color_scheme": "Yellow, Green, Maroon, Gold",
    "image_type": "Worn",
    "cultural_use": "Marriage ceremony",
    "notes": "Decorative border with classic checked body",
    "motif_type": "Checkered, Floral",
    "material": "Silk with Zari"
  },
  {
    "image_filename": "kancheepuram_silk_17.jpg",
    "fabric_name": "Kancheepuram Silk",
    "country_of_origin": "India",
    "color_scheme": "Red, Gold",
    "image_type": "Flat Display",
    "cultural_use": "Religious celebration",
    "notes": "Heavy brocade work on vibrant red silk",
    "motif_type": "Floral, Circular, Traditional",
    "material": "Silk with Zari"
  },
  {
    "image_filename": "kancheepuram_silk_18.jpg",
    "fabric_name": "Kancheepuram Silk",
    "country_of_origin": "India",
    "color_scheme": "Yellow, Purple, Gold",
    "image_type": "Flat Display",
    "cultural_use": "Cultural performance",
    "notes": "Elephant and floral border motifs",
    "motif_type": "Elephant, Floral, Traditional",
    "material": "Silk with Zari"
  }



]


df_kancheepuram = pd.DataFrame(kancheepuram_metadata)
df_kancheepuram.to_csv("kancheepuram_metadata.csv", index=False)
