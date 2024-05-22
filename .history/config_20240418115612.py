DEFAULT_API_KEY = "95babed2e072f2640bbdd8f179a6bfe0cad718d8939a84d604a9f4ebfcb03ad1ca9da58b98573e0eb572e09d9893f1c9795277d4b1264ca4dfc53600dcb7cbd3"
DEFAULT_SERVER = "https://ssj-pleasanterdev-sv.local.sdt-autolabo.com"
DEFAULT_SITE_ID = "2729117"

DOCUMENT_DIRECTORY = "C:/Users/NT-210174/Desktop/work/詳細設計書"

MARK_OK = "〇"


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
        "scope": "all",
    },
    "表示名": {
        "key": "LabelText",
        "type": "string",
        "scope": "all",
    },
    "配置": {
        "key": "TextAlign",
        "type": "array",
        "values": {
            "左寄せ" : 10,
            "右寄せ" : 20,
        },
        "scope": "all",
    },
    "スタイル": {
        "key": "FieldCss",
        "type": "array",
        "values": {
            "ノーマル" : "field-normal",
            "ワイド" : "field-wide",
        },
        "scope": "all",
    },
    "入力必須": {
        "key": "ValidateRequired",
        "type": "bool",
        "scope": "all",
    },
    "一括更新を許可": {
        "key": "AllowBulkUpdate",
        "type": "bool",
        "scope": "all",
    },
    "重複禁止": {
        "key": "NoDuplication",
        "type": "bool",
        "scope": "all",
    },
    "既定値でコピー": {
        "key": "CopyByDefault",
        "type": "bool",
        "scope": "all",
    },
    "読取専用": {
        "key": "EditorReadOnly",
        "type": "bool",
        "scope": "all",
    },
    "インポートのキー": {
        "key": "ImportKey",
        "type": "bool",
        "scope": "all",
    },
    "既定値": {
        "key": "DefaultInput",
        "type": "string",
        "scope": "all",
    },
    "書式": {
        "key": "Format",
        "type": "array",
        "values": {
            "標準" : "",
            "通貨" : "C",
            "桁区切り" : "N",
            "カスタム" : " ",
        },
        "scope": "all",
    },
    "NULL許容": {
        "key": "Nullable",
        "type": "bool",
        "scope": "all",
    },
    "単位": {
        "key": "Unit",
        "type": "string",
        "scope": "all",
    },
    "小数点以下桁数": {
        "key": "DecimalPlaces",
        "type": "float",
        "scope": "all",
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
        },
        "scope": "all",
    },
    "コントロール種別": {
        "key": "ChoicesControlType",
        "type": "array",
        "values": {
            "ドロップダウンリスト" : "DropDown",
            "ラジオボタン" : "Radio",
        },
        "scope": "all",
    },
    "最小": {
        "key": "Min",
        "type": "float",
        "scope": "all",
    },
    "最大": {
        "key": "Max",
        "type": "float",
        "scope": "all",
    },
    "説明": {
        "key": "Description",
        "type": "string",
        "scope": "all",
    },
    "自動ポストバック": {
        "key": "AutoPostBack",
        "type": "bool",
        "scope": "all",
    },
    "回り込みしない": {
        "key": "NoWrap",
        "type": "bool",
        "scope": "all",
    },
    "非表示": {
        "key": "Hide",
        "type": "bool",
        "scope": "all",
    },
    "フィールドCSS": {
        "key": "ExtendedFieldCss",
        "type": "string",
        "scope": "all",
    },
    "コントロールCSS": {
        "key": "ExtendedControlCss",
        "type": "string",
        "scope": "all",
    },
    "フルテキストの種類": {
        "key": "FullTextTypes",
        "type": "array",
        "values": {
            "無し" : 0,
            "表示名" : 1,
            "値" : 2,
            "値と表示名" : 3,
        },
        "scope": "all",
    },
    "最大文字数": {
        "key": "MaxLength",
        "type": "float",
        "scope": "all",
    },
    "選択肢一覧": {
        "key": "ChoicesText",
        "type": "textarea",
        "scope": "all",
    },
    "検索機能を使う": {
        "key": "UseSearch",
        "type": "bool",
        "scope": "all",
    },
    "複数選択": {
        "key": "MultipleSelections",
        "type": "bool",
        "scope": "all",
    },
    "選択肢にブランクを挿入しない": {
        "key": "NotInsertBlankChoice",
        "type": "bool",
        "scope": "all",
    },
    "アンカー": {
        "key": "Anchor",
        "type": "bool",
        "scope": "all",
    },
    "エディタの書式": {
        "key": "EditorFormat",
        "type": "array",
        "values": {
            "日付と時刻(秒)" : "Ymdhms",
            "年月日" : "Ymd",
            "日付と時刻(分)" : "Ymdhm",
        },
        "scope": "all",
    },
    "ビュワー切替": {
        "key": "ViewerSwitchingType",
        "type": "array",
        "values": {
            "自動" : 1,
            "手動" : 2,
            "無効" : 3,
        },
        "scope": "all",
    },
    "画像の登録を許可": {
        "key": "AllowImage",
        "type": "bool",
        "scope": "all",
    },
    "サムネイルサイズ": {
        "key": "ThumbnailLimitSize",
        "type": "float",
        "scope": "all",
    },
    "添付ファイルの削除を許可": {
        "key": "AllowDeleteAttachments",
        "type": "bool",
        "scope": "all",
    },
    "履歴に存在するファイルは削除しない": {
        "key": "NotDeleteExistHistory",
        "type": "bool",
        "scope": "all",
    },
    "同盟ファイルを上書きする": {
        "key": "OverwriteSameFileName",
        "type": "bool",
        "scope": "all",
    },
    "ファイル数制限": {
        "key": "LimitQuantity",
        "type": "float",
        "scope": "all",
    },
    "最容量制限(MB)": {
        "key": "LimitSize",
        "type": "float",
        "scope": "all",
    },
    "全最容量制限(MB)": {
        "key": "LimitTotalSize",
        "type": "float",
        "scope": "all",
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

site_post_json = {
	"TenantId": 1,
	# "SiteId": 1,
	"Title": "",
	# "Body": '',
	# "GridGuide": '',
	# "EditorGuide": '',
	"ReferenceType": 'Results',
	# "ParentId": 0,
	"SiteSettings": {
		"Version": 1.017,
		"ReferenceType": 'Results',
		"GridColumns": [],
		"FilterColumns": [],
		"EditorColumnHash": {
			"General": [],
		},
		# "TabLatestId": 0,
		# "Tabs": [],
		# "SectionLatestId": 0,
		# "Sections": [],
		"LinkColumns": [],
		"Columns": [],
		# "Links": [],
		"Exports": [],
		"Styles": [],
		"Scripts": [],
    # "TitleSeparator": '',
	# 	"NoDisplayIfReadOnly": False,
	},
	# "Publish": False,
	# "DisableCrossSearch": False,
	# "Comments": [],
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