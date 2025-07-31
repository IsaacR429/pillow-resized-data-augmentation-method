# Fabric Image Preprocessing Pipeline (Pillow)

This project contains a complete image preprocessing pipeline for a cultural fabric recognition dataset using **Pillow**. The dataset includes traditional fabrics from **Burkina Faso**, **Ghana**, and **India**, and is organized into subfolders for each country.



##  Project Structure

Fabrics_image/
├── Burkina_Faso_Fabrics/
├── Ghana_Fabrics/
├── India_Fabrics/

resized_fabrics_images/
├── burkina_faso_fabrics/
├── ghana_fabrics/
├── india_fabrics/




##  Purpose

Standardizing and augmenting images is a critical step before training a deep learning model. This pipeline prepares raw fabric images for use in classification tasks such as predicting the **country of origin** using CNNs.

---

##  Step 1: Image Standardization

###  Objective:
Ensure all images:
- Are square (equal width and height)
- Have the same resolution (224x224)
- Are in RGB format
- Are center-aligned with padding (not distorted by stretching)

###  Method:
We used **Pillow** to:
1. **Load images** using `Image.open()`
2. **Convert to RGB** using `convert("RGB")` to ensure 3 channels
3. **Center-pad non-square images** using `ImageOps.expand()`
   - White padding is used to avoid introducing color bias
4. **Resize all images** to `(224, 224)` using `.resize()`
5. **Save preprocessed images** into a new folder structure, preserving class labels

---

##  Step 2: Data Augmentation (Pillow)

###  Objective:
Increase data variability to avoid overfitting during training.

###  Augmentations Applied:
For each image:
1. **Horizontal Flip** → simulates fabric seen from different angles
2. **Rotation (-20°)** → helps model generalize to rotated patterns
3. **Brightness Enhancement (x1.5)** → simulates lighting variation

Each augmentation is saved as a separate image in the same subfolder.

---

##  Tools Used

- Python `os` module for file traversal
- `PIL.Image` for image loading and conversion
- `ImageOps.expand` for padding
- `ImageEnhance` for brightness control

---