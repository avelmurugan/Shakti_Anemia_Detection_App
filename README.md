# Shakti_Anemia_Detection_App
Shakti - Image Recognition tool to detect Anaemia

https://www.figma.com/file/xY1R9SyYXvBtQHJX8coOEN/Shakti?node-id=0%3A1&t=4Amtnz68zrB6AFfv-1

Detecting Anemia through Inner Eyelid Image Analysis in Women

Abstract:
This technical write-up proposes a novel approach to detect anemia in women using digital image analysis of the inner eyelid. The technique involves capturing high-resolution images of the inner eyelid, processing them with computer vision algorithms, and classifying the level of anemia using machine learning models. This non-invasive and rapid method can aid in early detection and monitoring of anemia, improving patient outcomes and reducing the need for traditional blood tests.

Introduction
Anemia, a common medical condition that affects women worldwide, is characterized by a deficiency in red blood cells or hemoglobin. Early detection and management of anemia are crucial to minimize the risk of complications. Currently, the gold standard for diagnosing anemia is a blood test. However, this method is invasive, time-consuming, and expensive. In this write-up, we propose a non-invasive approach that employs digital image analysis of the inner eyelid to detect anemia in women.

Data Collection
High-quality images of the inner eyelid can be captured using a smartphone or digital camera with appropriate lighting and magnification. Participants should be instructed to gently pull down their lower eyelid to expose the inner lining (palpebral conjunctiva) while avoiding strain or discomfort. The images should be captured in a controlled environment to ensure consistency in lighting and focus.

Image Preprocessing
The acquired images need to undergo preprocessing steps to enhance their quality and prepare them for analysis. These steps may include:

3.1. Color space conversion: Convert the images from the RGB color space to a more suitable color space, such as the Lab color space, to separate color information from luminance.
3.2. Image segmentation: Extract the region of interest (ROI), which is the inner eyelid, from the surrounding skin and eyelashes using edge detection and morphological operations.
3.3. Noise reduction: Apply smoothing filters (e.g., Gaussian blur) to reduce noise and artifacts in the images.
3.4. Contrast enhancement: Enhance the contrast of the segmented inner eyelid region to highlight the color differences.

Feature Extraction
Extract relevant features from the preprocessed images to represent the color and texture characteristics of the inner eyelid, such as mean, standard deviation, and skewness of the color channels, and textural features like entropy and contrast.

Anemia Classification
Train a machine learning model (e.g., Support Vector Machine, Random Forest, or Deep Learning) using a labeled dataset that includes both anemic and non-anemic women. The model should be optimized to classify the severity of anemia based on the extracted features from the inner eyelid images.

Model Validation
Evaluate the performance of the classification model using standard metrics like accuracy, sensitivity, specificity, and area under the Receiver Operating Characteristic (ROC) curve. Perform cross-validation to ensure the model's robustness and generalizability.

Conclusion
Detecting anemia through inner eyelid image analysis offers a non-invasive, rapid, and cost-effective alternative to traditional blood tests. This technique has the potential to improve early detection and monitoring of anemia in women, leading to better health outcomes and reduced healthcare costs. Further research and development are required to refine the method and validate its efficacy in diverse populations.
