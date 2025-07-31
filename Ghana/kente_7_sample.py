import pandas as pd

kente_metadata = [
    {
        "image_filename": "kente_sample_1.jpg",
        "fabric_name": "Kente",
        "country_of_origin": "Ghana",
        "color_scheme": "Yellow, Red, Blue",
        "image_type": "Worn",
        "cultural_use": "Royal ceremony",
        "notes": "Classic Ashanti wrap with traditional beads",
        "motif_type": "Geometric blocks, Zigzag, Rectangles",
        "material": "Cotton (loom-woven)"
    },
    {
        "image_filename": "kente_sample_2.jpg",
        "fabric_name": "Kente",
        "country_of_origin": "Ghana",
        "color_scheme": "Purple, Cream",
        "image_type": "Worn",
        "cultural_use": "Modern pride walk",
        "notes": "Contemporary take with hat and beads",
        "motif_type": "Geometric blocks, Zigzag, Rectangles",
        "material": "Cotton (loom-woven)"
    },
    {
        "image_filename": "kente_sample_3.jpg",
        "fabric_name": "Kente",
        "country_of_origin": "Ghana",
        "color_scheme": "Purple, Yellow",
        "image_type": "Worn",
        "cultural_use": "Cultural photography",
        "notes": "Regal style worn by woman with accessories",
        "motif_type": "Geometric blocks, Zigzag, Rectangles",
        "material": "Cotton (loom-woven)"
    },
    {
        "image_filename": "kente_sample_4.jpg",
        "fabric_name": "Kente",
        "country_of_origin": "Ghana",
        "color_scheme": "Orange, White, Purple",
        "image_type": "Close-up",
        "cultural_use": "Design study",
        "notes": "Lightning bolt motifs",
        "motif_type": "Geometric blocks, Zigzag, Rectangles",
        "material": "Cotton (loom-woven)"
    },
    {
        "image_filename": "kente_sample_5.jpg",
        "fabric_name": "Kente",
        "country_of_origin": "Ghana",
        "color_scheme": "Yellow, Green, Black",
        "image_type": "Close-up",
        "cultural_use": "Traditional design",
        "notes": "Rich symbolic geometric blocks",
        "motif_type": "Geometric blocks, Zigzag, Rectangles",
        "material": "Cotton (loom-woven)"
    },
    {
        "image_filename": "kente_sample_6.jpg",
        "fabric_name": "Kente",
        "country_of_origin": "Ghana",
        "color_scheme": "Teal, White, Yellow",
        "image_type": "Close-up",
        "cultural_use": "Modern textile variant",
        "notes": "Symmetrical horizontal layout",
        "motif_type": "Geometric blocks, Zigzag, Rectangles",
        "material": "Cotton (loom-woven)"
    },
    {
        "image_filename": "kente_sample_7.jpg",
        "fabric_name": "Kente",
        "country_of_origin": "Ghana",
        "color_scheme": "Orange, Green, Maroon",
        "image_type": "Close-up",
        "cultural_use": "Museum-style archive",
        "notes": "High-density pattern structure",
        "motif_type": "Geometric blocks, Zigzag, Rectangles",
        "material": "Cotton (loom-woven)"
    },
    {
        "image_filename": "kente_sample_9.jpg",
        "fabric_name": "Kente",
        "country_of_origin": "Ghana",
        "color_scheme": "Blue, Red, Yellow, Green",
        "image_type": "Worn",
        "cultural_use": "Royal occasion / Heritage shoot",
        "notes": "Man dressed in a traditional Ashanti wrap with bold gold jewelry",
        "motif_type": "Geometric blocks, Zigzag, Diamond, Triangle",
        "material": "Cotton (loom-woven)"
    },
    {
        "image_filename": "kente_sample_10.jpg",
        "fabric_name": "Kente",
        "country_of_origin": "Ghana",
        "color_scheme": "Yellow, Red, Green, Blue, Black",
        "image_type": "Flat cloth",
        "cultural_use": "General-purpose traditional cloth",
        "notes": "Block-printed version with repeating geometric motifs",
        "motif_type": "Stairs, Stripes, Triangles",
        "material": "Cotton (block print imitation)"
    },
    {
        "image_filename": "kente_sample_11.jpg",
        "fabric_name": "Kente",
        "country_of_origin": "Ghana",
        "color_scheme": "Red, Yellow, Green, Black",
        "image_type": "Worn",
        "cultural_use": "Runway / Cultural fashion event",
        "notes": "Modern kente interpretation with sashes and jewelry",
        "motif_type": "Checkerboard, Zigzag, Stripe",
        "material": "Cotton (loom-woven)"
    },
    {
        "image_filename": "kente_sample_12.jpg",
        "fabric_name": "Kente",
        "country_of_origin": "Ghana",
        "color_scheme": "Yellow, Blue, Green, Black",
        "image_type": "Flat cloth",
        "cultural_use": "Traditional celebrations",
        "notes": "Alternating checkerboard and triangle patterns",
        "motif_type": "Checkerboard, Triangles, Lines",
        "material": "Cotton (loom-woven)"
    },
    {
        "image_filename": "kente_sample_13.jpg",
        "fabric_name": "Kente",
        "country_of_origin": "Ghana",
        "color_scheme": "Orange, Blue, Black, Green",
        "image_type": "Flat cloth",
        "cultural_use": "Ceremonial attire",
        "notes": "High pattern density with center motifs and vertical symmetry",
        "motif_type": "Chevron, Diamond, Zigzag",
        "material": "Cotton (loom-woven)"
    },
    {
        "image_filename": "kente_sample_14.jpg",
        "fabric_name": "Kente",
        "country_of_origin": "Ghana",
        "color_scheme": "Orange, Blue, Green, Black",
        "image_type": "Flat cloth",
        "cultural_use": "Traditional fabric for tailored garments",
        "notes": "Vertical motifs separated by bands, iconic chevron triangles",
        "motif_type": "Chevron, Lines, Vertical bands",
        "material": "Cotton (loom-woven)"
    },
    {
        "image_filename": "kente_sample_15.jpg",
        "fabric_name": "Kente",
        "country_of_origin": "Ghana",
        "color_scheme": "Green, Yellow, Purple",
        "image_type": "Worn",
        "cultural_use": "Cultural photo shoot",
        "notes": "Styled as crop top and skirt with accessories",
        "motif_type": "Zigzag, Triangles, Vertical Stripes",
        "material": "Cotton (loom-woven)"
    },
    {
        "image_filename": "kente_sample_16.jpg",
        "fabric_name": "Kente",
        "country_of_origin": "Ghana",
        "color_scheme": "Green, Yellow, Orange, Blue",
        "image_type": "Worn",
        "cultural_use": "Cultural modeling / Heritage event",
        "notes": "Kente wrap styled with beads and pot, vibrant contrast",
        "motif_type": "Checkerboard, Diamond, Stripe",
        "material": "Cotton (loom-woven)"
    },
    {
        "image_filename": "kente_sample_17.jpg",
        "fabric_name": "Kente",
        "country_of_origin": "Ghana",
        "color_scheme": "Purple, Orange, White",
        "image_type": "Worn",
        "cultural_use": "Modern fashion interpretation",
        "notes": "Kente with bold purple diamonds and crisscross patterns",
        "motif_type": "Diamond grid, Crosshatch, Zigzag",
        "material": "Cotton (loom-woven)"
    },
    {
        "image_filename": "kente_sample_18.jpg",
        "fabric_name": "Kente",
        "country_of_origin": "Ghana",
        "color_scheme": "Green, Red, Orange, Yellow",
        "image_type": "Worn",
        "cultural_use": "Wedding / engagement attire",
        "notes": "Tailored dress combining kente patches and modern fit",
        "motif_type": "Patchwork, Stripe, Square motifs",
        "material": "Cotton-blend (loom-woven)"
    }
]


df_kente = pd.DataFrame(kente_metadata)

df_kente.to_csv("kente_metadata.csv", index=False)
