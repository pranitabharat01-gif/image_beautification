import pickle
from app.pipeline import ImageEnhancerPipeline

# Create pipeline instance with desired config
pipeline = ImageEnhancerPipeline(contrast_factor=1.5)

# Save pipeline to pickle file
with open('image_pipeline.pkl', 'wb') as f:
    pickle.dump(pipeline, f)

print("✅ Pipeline pickled as 'image_pipeline.pkl'")
