import pandas as pd

KEY_COLUMNS = [
    "Comp_ID"
]


def load_checklist(file_path):
    return pd.read_excel(file_path)


def create_key(df):
    return (
        df[KEY_COLUMNS]
        .fillna("")
        .astype(str)
        .agg("|".join, axis=1)
    )


def compare_checklists(old_file, new_file):

    old_df = load_checklist(old_file)
    new_df = load_checklist(new_file)

    old_df["_key"] = create_key(old_df)
    new_df["_key"] = create_key(new_df)

    old_keys = set(old_df["_key"])
    new_keys = set(new_df["_key"])

    added_keys = new_keys - old_keys
    deleted_keys = old_keys - new_keys
    common_keys = old_keys.intersection(new_keys)

    added = new_df[
        new_df["_key"].isin(added_keys)
    ]

    deleted = old_df[
        old_df["_key"].isin(deleted_keys)
    ]

    modified_rows = []

    for key in common_keys:

        old_row = (
            old_df[old_df["_key"] == key]
            .iloc[0]
            .drop("_key")
        )

        new_row = (
            new_df[new_df["_key"] == key]
            .iloc[0]
            .drop("_key")
        )

        if not old_row.equals(new_row):

            modified_rows.append({
                "key": key,
                "old": old_row.to_dict(),
                "new": new_row.to_dict()
            })

    return {
        "added": added.drop(columns="_key"),
        "deleted": deleted.drop(columns="_key"),
        "modified": modified_rows,
        "summary": {
            "added": len(added),
            "deleted": len(deleted),
            "modified": len(modified_rows),
            "total_new": len(new_df)
        }
    }