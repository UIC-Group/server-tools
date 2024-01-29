import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-server-tools",
    description="Meta package for oca-server-tools Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-attachment_queue>=16.0dev,<16.1dev',
        'odoo-addon-attachment_unindex_content>=16.0dev,<16.1dev',
        'odoo-addon-auditlog>=16.0dev,<16.1dev',
        'odoo-addon-auto_backup>=16.0dev,<16.1dev',
        'odoo-addon-base_cron_exclusion>=16.0dev,<16.1dev',
        'odoo-addon-base_domain_inverse_function>=16.0dev,<16.1dev',
        'odoo-addon-base_exception>=16.0dev,<16.1dev',
        'odoo-addon-base_fontawesome>=16.0dev,<16.1dev',
        'odoo-addon-base_m2m_custom_field>=16.0dev,<16.1dev',
        'odoo-addon-base_name_search_improved>=16.0dev,<16.1dev',
        'odoo-addon-base_partition>=16.0dev,<16.1dev',
        'odoo-addon-base_search_fuzzy>=16.0dev,<16.1dev',
        'odoo-addon-base_sequence_default>=16.0dev,<16.1dev',
        'odoo-addon-base_sequence_option>=16.0dev,<16.1dev',
        'odoo-addon-base_sparse_field_list_support>=16.0dev,<16.1dev',
        'odoo-addon-base_technical_user>=16.0dev,<16.1dev',
        'odoo-addon-base_time_window>=16.0dev,<16.1dev',
        'odoo-addon-base_view_inheritance_extension>=16.0dev,<16.1dev',
        'odoo-addon-cron_daylight_saving_time_resistant>=16.0dev,<16.1dev',
        'odoo-addon-database_cleanup>=16.0dev,<16.1dev',
        'odoo-addon-dbfilter_from_header>=16.0dev,<16.1dev',
        'odoo-addon-excel_import_export>=16.0dev,<16.1dev',
        'odoo-addon-excel_import_export_demo>=16.0dev,<16.1dev',
        'odoo-addon-excel_import_export_unidecode>=16.0dev,<16.1dev',
        'odoo-addon-html_text>=16.0dev,<16.1dev',
        'odoo-addon-iap_alternative_provider>=16.0dev,<16.1dev',
        'odoo-addon-jsonifier>=16.0dev,<16.1dev',
        'odoo-addon-module_analysis>=16.0dev,<16.1dev',
        'odoo-addon-module_auto_update>=16.0dev,<16.1dev',
        'odoo-addon-module_change_auto_install>=16.0dev,<16.1dev',
        'odoo-addon-onchange_helper>=16.0dev,<16.1dev',
        'odoo-addon-rpc_helper>=16.0dev,<16.1dev',
        'odoo-addon-scheduler_error_mailer>=16.0dev,<16.1dev',
        'odoo-addon-sentry>=16.0dev,<16.1dev',
        'odoo-addon-session_db>=16.0dev,<16.1dev',
        'odoo-addon-tracking_manager>=16.0dev,<16.1dev',
        'odoo-addon-upgrade_analysis>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
