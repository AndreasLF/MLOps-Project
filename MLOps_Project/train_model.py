from pytorch_lightning import Trainer
from pytorch_lightning.loggers import WandbLogger
from MLOps_Project.data.fashion_mnist_dataset import get_dataloaders
import hydra
from omegaconf import DictConfig


# Call when training!
@hydra.main(version_base=None, config_path="../configs", config_name="config")
def train(cfg: DictConfig):
    # Initialize logger and save experiment hyperparameters
    wandb_logger = WandbLogger(project='FashionMNIST')
    wandb_logger.experiment.config.update(dict(cfg.architecture))

    # Create custom datasets and dataloaders
    train_dataloader, val_dataloader, test_dataloader = get_dataloaders(cfg)

    # Test Training
    model = hydra.utils.instantiate(cfg.architecture)
    print(model)

    trainer = Trainer(callbacks=model.callbacks, max_epochs=cfg.training.max_epochs, logger=wandb_logger)
    trainer.fit(model, train_dataloader, val_dataloader)

    print("!!! DONE !!!")


# Entrypoint
if __name__ == "__main__":
    train()
