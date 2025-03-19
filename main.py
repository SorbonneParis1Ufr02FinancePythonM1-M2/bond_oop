import repository as repo
import view
from model import add_bonds_properties


def main():
    print("begin program")
    bonds = repo.get_data()
    bonds_results = add_bonds_properties(bonds)
    view.to_json(bonds_results)
    view.to_csv(bonds_results)
    view.to_excel(bonds_results)
    print("end program")


if __name__ == "__main__":
    main()
