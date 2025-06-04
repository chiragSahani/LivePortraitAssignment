import gradio as gr
from gradio.components import Radio

with gr.Blocks(theme=gr.themes.Soft(font=[gr.themes.GoogleFont("Plus Jakarta Sans")])) as demo:
    gr.HTML(load_description(title_md))

    # Add mode selector
    mode_selector = gr.Radio(["Quality", "Fast"], value="Quality", label="Mode (Speed vs. Quality)")

    gr.Markdown(load_description("assets/gradio/gradio_description_upload.md"))

# Before launching Gradio, patch the pipeline config based on mode

def set_mode(mode, pipeline):
    if mode == "Fast":
        pipeline.args.input_shape = (128, 128)
        pipeline.args.source_max_dim = 512
    else:
        pipeline.args.input_shape = (256, 256)
        pipeline.args.source_max_dim = 1280
    # Also update the underlying config objects if needed
    if hasattr(pipeline, 'live_portrait_wrapper'):
        pipeline.live_portrait_wrapper.inference_cfg.input_shape = pipeline.args.input_shape
    if hasattr(pipeline, 'cropper'):
        pipeline.cropper.crop_cfg.input_shape = pipeline.args.input_shape
    return None

# Bind mode selector to set_mode
mode_selector.change(fn=lambda mode: set_mode(mode, gradio_pipeline), inputs=mode_selector, outputs=None)

demo.launch(
    server_port=args.server_port,
    share=args.share,
    server_name=args.server_name
) 