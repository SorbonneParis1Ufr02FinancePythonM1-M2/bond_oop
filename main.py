import repository as repo
import view
from model import add_bonds_properties


def main():
    print("begin program")
    config = repo.get_config()
    bonds = repo.get_data(config)
    # bonds_results = add_bonds_properties(bonds, config)
    view.to_print(bonds, config)
    # view.to_json(bonds, config)
    # view.to_csv(bonds, config)
    # view.to_excel(bonds, config)
    print("end program")


if __name__ == "__main__":
    main()
