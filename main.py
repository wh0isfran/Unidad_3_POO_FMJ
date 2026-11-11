from config.database import Database
from controllers.main_controller import MainController

def main() -> None:
    print("Inicializando sistema...")
    db = Database()
    db.init_db()
    
    app = MainController()
    app.ejecutar()

if __name__ == "__main__":
    main()