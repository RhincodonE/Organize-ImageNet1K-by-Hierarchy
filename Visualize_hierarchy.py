import plotly.graph_objects as go
import os
import argparse

def build_plotly_hierarchy(root_dir):
    ids = []
    labels = []
    parents = []

    for dirpath, dirnames, _ in os.walk(root_dir):
        for dirname in dirnames:
            full_path = os.path.join(dirpath, dirname)
            # Use relative path as ID to ensure uniqueness
            rel_path = os.path.relpath(full_path, root_dir)
            ids.append(rel_path)
            labels.append(dirname)
            # Parent directory's relative path
            parent_path = os.path.relpath(os.path.dirname(full_path), root_dir)
            parents.append(parent_path if parent_path != '.' else "")

    # Add root element
    ids.append('')
    labels.append(os.path.basename(root_dir))
    parents.append('')

    return ids, labels, parents

def main(root_dir):
    # Generate data for the hierarchy
    ids, labels, parents = build_plotly_hierarchy(root_dir)

    # Create the treemap
    fig = go.Figure(go.Treemap(
        ids=ids,
        labels=labels,
        parents=parents,
    ))

    fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))

    # Show the figure
    fig.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Visualize directory hierarchy as an interactive treemap.')
    parser.add_argument('root_dir', type=str, help='Root directory for building the hierarchy visualization.')

    args = parser.parse_args()

    main(args.root_dir)
