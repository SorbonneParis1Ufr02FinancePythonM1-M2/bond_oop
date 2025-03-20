import repository as repo
import view
from model import add_bonds_properties


def main():
    print("begin program")
    config = repo.get_config()
    bonds = repo.get_data(config)
    bonds_results = add_bonds_properties(bonds, config)
    view.to_json(bonds_results, config)
    view.to_csv(bonds_results, config)
    view.to_excel(bonds_results, config)
    print("end program")


if __name__ == "__main__":
    main()
