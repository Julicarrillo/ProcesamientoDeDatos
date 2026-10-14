
import os
import matplotlib.pyplot as plt

def plot_disasters_by_year(counts, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    fig, ax = plt.subplots(figsize=(12, 5))

    counts.plot(kind="line", ax=ax, marker="o")

    ax.set_title("Evolución de los desastres naturales (1970-2021)")
    ax.set_xlabel("Año")
    ax.set_ylabel("Cantidad de desastres")
    ax.grid(True)

    fig.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)


def plot_disasters_by_type_continent(tabla, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    principales = tabla.loc[
        tabla.sum(axis=1).nlargest(5).index
    ]

    ax = principales.plot(
        kind="bar",
        figsize=(12, 6)
    )

    ax.set_title("Principales tipos de desastres por continente")
    ax.set_xlabel("Tipo de desastre")
    ax.set_ylabel("Cantidad de desastres")
    ax.legend(title="Continente")

    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def plot_disasters_by_month(counts, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    fig, ax = plt.subplots(figsize=(10, 5))

    counts.plot(kind="bar", ax=ax)

    ax.set_title("Distribución mensual de desastres naturales (1970-2021)")
    ax.set_xlabel("Mes")
    ax.set_ylabel("Cantidad de desastres")
    ax.set_xticklabels(
        ["Ene", "Feb", "Mar", "Abr", "May", "Jun",
         "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"],
        rotation=0
    )

    fig.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)


def plot_disasters_by_type_year(tabla, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    fig, ax = plt.subplots(figsize=(12, 6))

    tabla.plot(kind="line", ax=ax, marker="o")

    ax.set_title("Evolución de los principales desastres (2002-2021)")
    ax.set_xlabel("Año")
    ax.set_ylabel("Cantidad de desastres")
    ax.legend(title="Tipo de desastre")
    ax.grid(True)

    fig.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)


def plot_affected_by_continent(tabla, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    fig, ax = plt.subplots(figsize=(10, 5))

    tabla["sum"].plot(kind="bar", ax=ax)

    ax.set_title("Personas afectadas por continente (1970-2021)")
    ax.set_xlabel("Continente")
    ax.set_ylabel("Total de personas afectadas registradas")

    plt.xticks(rotation=0)
    fig.tight_layout()
    fig.savefig(output_path)
    plt.close(fig)
