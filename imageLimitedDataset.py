import os
from torchvision.datasets.folder import ImageFolder
from typing import Callable, List, Optional, Tuple, Dict, Any

class ImageLimitedDataset(ImageFolder):
  """A data loader that implements slices for ImageFolder.

  Args:
      slices (list, optional): A list of slices used to keep only a certain number of samples.
          For the class with index i the slice at index i % len(slices) is used.
      check_images (boolean, default True): If True, check if there are files that cannot be
          read by PIL. The creation of the dataset will be slower.
  """

  def is_valid_image(self, path: str) -> bool:
    if not os.path.exists(path):
      return False

    img = None
    try:
      img = self.loader(path)
    except:
      return False

    return img is not None

  def make_dataset(
      self,
      directory: str,
      class_to_idx: Dict[str, int],
      extensions: Optional[Tuple[str, ...]] = None,
      is_valid_file: Optional[Callable[[str], bool]] = None,
  ) -> List[Tuple[str, int]]:
    """Generates a list of samples of a form (path_to_sample, class).
    
    If specified, it cuts the dataset using slices passed to the constructor.
    """
    directory = os.path.expanduser(directory)

    instances = []

    available_classes = set()
    for target_class in sorted(class_to_idx.keys()):
      class_index = class_to_idx[target_class]
      target_dir = os.path.join(directory, target_class)
      if not os.path.isdir(target_dir):
        continue

      class_instances = []

      for root, _, fnames in sorted(os.walk(target_dir, followlinks=True)):
        for fname in sorted(fnames):
          path = os.path.join(root, fname)

          if extensions:
            _, fileextension = os.path.splitext(path)
            if not fileextension.lower() in extensions:
              print("[🛑 ERROR] Found non valid extension:", path)
              continue

          if is_valid_file and not is_valid_file(path):
            print("[🛑 ERROR] Found non valid sample:", path)
            continue

          item = path, class_index
          class_instances.append(item)

          if target_class not in available_classes:
              available_classes.add(target_class)

      if self.slices:
        try:
          class_slice = self.slices[class_index % len(self.slices)]
        except:
          raise ValueError("[🛑 ERROR] Invalid slices:", self.slices)

        try:
          class_instances = class_instances[class_slice]
        except:
          raise ValueError("[🛑 ERROR] Invalid slice:", class_slice)

      instances.extend(class_instances)

    empty_classes = set(class_to_idx.keys()) - available_classes
    if empty_classes:
        msg = f"[🛑 ERROR] Found no valid file for the classes {', '.join(sorted(empty_classes))}. "
        if extensions is not None:
            msg += f"[🛑 ERROR] Supported extensions are: {', '.join(extensions)}"
        raise FileNotFoundError(msg)

    return instances

  def __init__(self, root: str,
               transform: Optional[Callable] = None,
               target_transform: Optional[Callable] = None,
               slices: Optional[List[slice]] = None,
               check_images: Optional[bool] = True,
               use_cache: Optional[bool] = False):

    self.slices = slices
    self.use_cache = use_cache
    self.cached_data = {}

    super().__init__(root, transform=transform,
                     target_transform=target_transform,
                     is_valid_file=self.is_valid_image if check_images else None)

  def __getitem__(self, index: int) -> Tuple[Any, Any]:
    path, _ = self.samples[index]

    if self.use_cache and path in self.cached_data.keys():
        return self.cached_data[path]

    sample, target = super().__getitem__(index)

    if self.use_cache:
      self.cached_data[path] = (sample, target)

    return sample, target
