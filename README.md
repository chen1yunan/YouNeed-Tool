# YouNeed-Tool
YouNeed-Tool : A tool to test GPUs (H100/H800/A100/A800/L40s/L40...) Flops running in different infrastructure environment (Training / Inference Flops testing). <br><br>
<img src="https://pic.imgdb.cn/item/65c1beb39f345e8d03eb6ac7.png" alt="Image" title="Image" width="246" height="200" />


## Notice

**[Background]** Due to the gap between products shown in the white book and actual performance. <br><br>
YouNeed-Tool aims to build a tool that helps users test their GPUs' true Flops performance. It can enable engineers to deeply understand the structural performance and **improve AI-HPC (High-performance computing) efficiency**.


**[Introdctuion]** The tool will randomly update popular LLM models in Hugging Face, including varied precision testing (FP32, FP16, BF16...). For more details, refer to the 'Details' section in this document.



## Details

The details provide the available models list and framework used in this tool:<br>

| | Name | Version|
|-|-|-|
| Training | Colossal-AI | >=0.3.3 |
| Inference | TensorRT-LLM | / |
<br>

| Model-Name | Precision|
|-|-|
 Colossal-LLaMA-2-7B |  |
|Colossal-LLaMA-2-13B |  |
| LLaMA-2-7B |  |
|  LLaMA-2-13B |  |

## Installation
- PyTorch >= 1.11 and PyTorch <= 2.1
- Python >= 3.7
- CUDA >= 11.0
- [NVIDIA GPU Compute Capability](https://developer.nvidia.com/cuda-gpus) >= 7.0 (V100/RTX20 and higher)
- Linux OS
```bash
pip install colossalai
```

**Note: only Linux is supported for now.**

However, if you want to build the PyTorch extensions during installation, you can set `CUDA_EXT=1`.

```bash
CUDA_EXT=1 pip install colossalai
```

## Latest Announcement