DEFAULT_API_KEY = "95babed2e072f2640bbdd8f179a6bfe0cad718d8939a84d604a9f4ebfcb03ad1ca9da58b98573e0eb572e09d9893f1c9795277d4b1264ca4dfc53600dcb7cbd3"
DEFAULT_SERVER = "https://ssj-pleasanterdev-sv.local.sdt-autolabo.com"
DEFAULT_SITE_ID = "2729117"

DOCUMENT_DIRECTORY = "C:/Users/NT-210174/Desktop/work/詳細設計書"

MARK_OK = "〇"

SHEET_NAME_EDITOR = "詳細_編集要素"
SHEET_NAME_LAYOUT = "一覧_画面レイアウト"

EDIT_ROW_INDEX_TYPE = 8
EDIT_ROW_INDEX_ITEM = 9
EDIT_ROW_INDEX_GRID = 10

LAYOUT_ROW_INDEX_TYPE = 38
LAYOUT_ROW_INDEX_GRID = 40

# タブの定義
TABS = {
    "一覧要素": {
        "key": 'GridColumns',
    },
    "集計要素": {
        "key": 'Aggregations',
    },
    "フィルタ要素": {
        "key": 'FilterColumns',
    },
    "編集要素": {
        "key": 'EditorColumnHash',
    },
    "リンク要素": {
        "key": 'LinkColumns',
    },
    "その他要素": {
        "key": 'others',
    },
}

# 型の定義
TYPES = {
    #"タイトル": {
    #    "key": 'Title',
    #},
    #"内容": {
    #    "key": 'Body',
    #},
    #"完了": {
    #    "key": 'CompletionTime',
    #},
    "分類項目": {
        "key": 'Class',
    },
    "数値項目": {
        "key": 'Num',
    },
    "日付項目": {
        "key": 'Date',
    },
    "説明項目": {
        "key": 'Description',
    },
    "チェック項目": {
        "key": 'Check',
    },
    "添付ファイル項目": {
        "key": 'Attachments',
    },
    #"見出し": {
    #    "key": 'Section',
    #},
}

# パラメータの定義
PARAMETERS = {
    "項目名": {
        "key": "ColumnName",
        "type": "string",
    },
    "表示名": {
        "key": "LabelText",
        "type": "string",
    },
    "配置": {
        "key": "TextAlign",
        "type": "array",
        "values": {
            "左寄せ" : 10,
            "右寄せ" : 20,
        }
    },
    "スタイル": {
        "key": "FieldCss",
        "type": "array",
        "values": {
            "ノーマル" : "field-normal",
            "ワイド" : "field-wide",
        }
    },
    "入力必須": {
        "key": "ValidateRequired",
        "type": "bool",
    },
    "一括更新を許可": {
        "key": "AllowBulkUpdate",
        "type": "bool",
    },
    "重複禁止": {
        "key": "NoDuplication",
        "type": "bool",
    },
    "既定値でコピー": {
        "key": "CopyByDefault",
        "type": "bool",
    },
    "読取専用": {
        "key": "EditorReadOnly",
        "type": "bool",
    },
    "インポートのキー": {
        "key": "ImportKey",
        "type": "bool",
    },
    "既定値": {
        "key": "DefaultInput",
        "type": "string",
    },
    "書式": {
        "key": "Format",
        "type": "array",
        "values": {
            "標準" : "",
            "通貨" : "C",
            "桁区切り" : "N",
            "カスタム" : " ",
        }
    },
    "NULL許容": {
        "key": "Nullable",
        "type": "bool",
    },
    "単位": {
        "key": "Unit",
        "type": "string",
    },
    "小数点以下桁数": {
        "key": "DecimalPlaces",
        "type": "float",
    },
    "端数処理種類": {
        "key": "RoundingType",
        "type": "array",
        "values": {
            "四捨五入" : 10,
            "切り上げ" : 20,
            "切り捨て" : 30,
            "切り下げ" : 40,
            "銀行家の丸め" : 50,
        }
    },
    "コントロール種別": {
        "key": "ChoicesControlType",
        "type": "array",
        "values": {
            "ドロップダウンリスト" : "DropDown",
            "ラジオボタン" : "Radio",
        }
    },
    "最小": {
        "key": "Min",
        "type": "float",
    },
    "最大": {
        "key": "Max",
        "type": "float",
    },
    "説明": {
        "key": "Description",
        "type": "string",
    },
    "自動ポストバック": {
        "key": "AutoPostBack",
        "type": "bool",
    },
    "回り込みしない": {
        "key": "NoWrap",
        "type": "bool",
    },
    "非表示": {
        "key": "Hide",
        "type": "bool",
    },
    "フィールドCSS": {
        "key": "ExtendedFieldCss",
        "type": "string",
    },
    "コントロールCSS": {
        "key": "ExtendedControlCss",
        "type": "string",
    },
    "フルテキストの種類": {
        "key": "FullTextTypes",
        "type": "array",
        "values": {
            "無し" : 0,
            "表示名" : 1,
            "値" : 2,
            "値と表示名" : 3,
        }
    },
    "最大文字数": {
        "key": "MaxLength",
        "type": "float",
    },
    "選択肢一覧": {
        "key": "ChoicesText",
        "type": "textarea",
    },
    "検索機能を使う": {
        "key": "UseSearch",
        "type": "bool",
    },
    "複数選択": {
        "key": "MultipleSelections",
        "type": "bool",
    },
    "選択肢にブランクを挿入しない": {
        "key": "NotInsertBlankChoice",
        "type": "bool",
    },
    "アンカー": {
        "key": "Anchor",
        "type": "bool",
    },
    "エディタの書式": {
        "key": "EditorFormat",
        "type": "array",
        "values": {
            "日付と時刻(秒)" : "Ymdhms",
            "年月日" : "Ymd",
            "日付と時刻(分)" : "Ymdhm",
        }
    },
    "ビュワー切替": {
        "key": "ViewerSwitchingType",
        "type": "array",
        "values": {
            "自動" : 1,
            "手動" : 2,
            "無効" : 3,
        }
    },
    "画像の登録を許可": {
        "key": "AllowImage",
        "type": "bool",
    },
    "サムネイルサイズ": {
        "key": "ThumbnailLimitSize",
        "type": "float",
    },
    "添付ファイルの削除を許可": {
        "key": "AllowDeleteAttachments",
        "type": "bool",
    },
    "履歴に存在するファイルは削除しない": {
        "key": "NotDeleteExistHistory",
        "type": "bool",
    },
    "同盟ファイルを上書きする": {
        "key": "OverwriteSameFileName",
        "type": "bool",
    },
    "ファイル数制限": {
        "key": "LimitQuantity",
        "type": "float",
    },
    "最容量制限(MB)": {
        "key": "LimitSize",
        "type": "float",
    },
    "全最容量制限(MB)": {
        "key": "LimitTotalSize",
        "type": "float",
    },
}

template_json = {

	"HeaderInfo": {
        "BaseSiteId": 1,
        "CreatorName": "Y-Sasaki",

		"Convertors": [
			{
				"SiteId": 1,
				"SiteTitle": "",
				"ReferenceType": "Results",
				"IncludeData": False
			}
		],
		"IncludeSitePermission": True,
		"IncludeRecordPermission": True,
		"IncludeColumnPermission": True,
        "IncludeNotifications": True,
        "IncludeReminders": True
	},
    "Sites": [],
	"Data": [],
	"Permissions": [
		{
			"SiteId": 1,
			"Permissions": []
		}
	],
	"PermissionIdList": {
		"DeptIdList": [],
		"GroupIdList": [],
		"UserIdList": []
	}
}

site_skeleton_json = {
	"TenantId": 1,
	"SiteId": 1,
	"Title": "",
	"Body": '',
	"GridGuide": '',
	"EditorGuide": '',
	"ReferenceType": 'Results',
	"ParentId": 0,
	"InheritPermission": 0,
	"SiteSettings": {
		"Version": 1.017,
		"ReferenceType": 'Results',
		"GridColumns": [],
		"FilterColumns": [],
		"EditorColumnHash": {
			"General": [],
		},
		"TabLatestId": 0,
		"Tabs": [],
		"SectionLatestId": 0,
		"Sections": [],
		"LinkColumns": [],
		"Columns": [],
		"Links": [],
		"Exports": [],
		"Styles": [],
		"Scripts": [],
    "TitleSeparator": '',
		"NoDisplayIfReadOnly": False,
	},
	"Publish": False,
	"DisableCrossSearch": False,
	"Comments": [],
}