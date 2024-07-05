import torch
from transformers import pipeline, CLIPTextModel, CLIPTokenizer, CLIPFeatureExtractor
from diffusers import StableDiffusionPipeline, AutoencoderKL, UNet2DConditionModel, PNDMScheduler 
from diffusers.pipelines.stable_diffusion.safety_checker import StableDiffusionSafetyChecker

model_id = "meta-llama/Meta-Llama-3-8B"
text_generator = pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto"
)

vae = AutoencoderKL.from_pretrained("stabilityai/stable-diffusion-3-medium-diffusers/vae")
tokenizer = CLIPTokenizer.from_pretrained("stabilityai/stable-diffusion-3-medium-diffusers/tokenizer")
scheduler = PNDMScheduler.from_pretrained("stabilityai/stable-diffusion-3-medium-diffusers/scheduler")
text_encoder = CLIPTextModel.from_pretrained("stabilityai/stable-diffusion-3-medium-diffusers/text_encoder")
unet = UNet2DConditionModel.from_pretrained("stabilityai/stable-diffusion-3-medium-diffusers/unet")
feature_extractor = CLIPFeatureExtractor.from_pretrained("stabilityai/stable-diffusion-3-medium-diffusers/feature_extractor")
safety_checker = StableDiffusionSafetyChecker.from_pretrained("stabilityai/stable-diffusion-3-medium-diffusers/safety_checker")

image_pipe = StableDiffusionPipeline(
    vae=vae,
    tokenizer=tokenizer,
    scheduler=scheduler,
    text_encoder=text_encoder,
    unet=unet,
    feature_extractor=feature_extractor,
    safety_checker=safety_checker,
    torch_dtype=torch.float16
)

image_pipe = image_pipe.to("cuda")

def generate_poem(prompt, max_length):
    result = text_generator(prompt, max_length=max_length, num_return_sequences=1)
    poem = result[0]['generated_text']
    return poem

def generate_image(prompt, negative_prompt, num_inference_steps, guidance_scale):
    image = image_pipe(
        prompt,
        negative_prompt=negative_prompt,
        num_inference_steps=num_inference_steps,
        guidance_scale=guidance_scale
    ).images[0]
    return image
