from gliner import GLiNER

import warnings

warnings.filterwarnings("ignore")

model = GLiNER.from_pretrained(
    "./",
    local_files_only=True,
    max_length=512,
)

default_labels = [
    "Brand",
    "Product",
    "Organization",
    "Person",
    "Event",
    "Misc",
    "Location",
    "Service",
    "Industry",
    "Technology",
    "Hobby",
    "Fashion",
    "Automobile",
    "Food",
    "Entertainment",
]
