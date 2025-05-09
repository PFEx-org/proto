# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: user.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'user.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
import common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nuser.proto\x12\x04user\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x0c\x63ommon.proto\"\x1e\n\x0bUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"!\n\x10UserEmailRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\"5\n\x0cUserFeeGroup\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x14\n\x0c\x66\x65\x65_group_id\x18\x02 \x01(\t\";\n\x0fUserMarginGroup\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x17\n\x0fmargin_group_id\x18\x02 \x01(\t\"\x8c\x01\n\nUserPublic\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x14\n\x0cis_superuser\x18\x03 \x01(\x08\x12\x16\n\x0eis_institution\x18\x04 \x01(\x08\x12\x11\n\tis_active\x18\x05 \x01(\x08\x12\x0f\n\x07\x61pi_key\x18\x06 \x01(\t\x12\x11\n\tfull_name\x18\x07 \x01(\t\"\xc9\x01\n\x0bUserPrivate\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x14\n\x0cis_superuser\x18\x03 \x01(\x08\x12\x16\n\x0eis_institution\x18\x04 \x01(\x08\x12\x11\n\tis_active\x18\x05 \x01(\x08\x12\x0f\n\x07\x61pi_key\x18\x06 \x01(\t\x12\x11\n\tfull_name\x18\x07 \x01(\t\x12\x17\n\x0fhashed_password\x18\x08 \x01(\t\x12\x0e\n\x06\x66\x65\x65_id\x18\t \x01(\t\x12\x11\n\tmargin_id\x18\n \x01(\t\"<\n\x0bUsersPublic\x12\x1e\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x10.user.UserPublic\x12\r\n\x05\x63ount\x18\x02 \x01(\x03\"G\n\x11\x43reateUserRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x11\n\tfull_name\x18\x03 \x01(\t\"4\n\x12UserCreateResponse\x12\x1e\n\x04user\x18\x01 \x01(\x0b\x32\x10.user.UserPublic\"/\n\x10ReadUsersRequest\x12\x0c\n\x04skip\x18\x01 \x01(\x05\x12\r\n\x05limit\x18\x02 \x01(\x05\"\xaa\x04\n\x12\x41ppendTradeRequest\x12\x10\n\x08trade_id\x18\x01 \x01(\t\x12\x0e\n\x06symbol\x18\x02 \x01(\t\x12.\n\x0e\x61ggressor_side\x18\x03 \x01(\x0e\x32\x16.common.OrderDirection\x12\x13\n\x0b\x62uy_user_id\x18\x04 \x01(\t\x12\x14\n\x0csell_user_id\x18\x05 \x01(\t\x12\x14\n\x0c\x62uy_order_id\x18\x06 \x01(\t\x12\x15\n\rsell_order_id\x18\x07 \x01(\t\x12\x0f\n\x07\x62uy_fee\x18\x08 \x01(\x04\x12\x10\n\x08sell_fee\x18\t \x01(\x04\x12\x10\n\x08quantity\x18\x0c \x01(\x04\x12\r\n\x05price\x18\r \x01(\x04\x12\x35\n\x13\x62uyer_time_in_force\x18\x0e \x01(\x0e\x32\x18.common.OrderTimeInForce\x12\x19\n\x11\x62uyer_order_price\x18\x0f \x01(\x04\x12\x36\n\x14seller_time_in_force\x18\x10 \x01(\x0e\x32\x18.common.OrderTimeInForce\x12\x1a\n\x12seller_order_price\x18\x11 \x01(\x04\x12\x1b\n\x13\x62uy_client_order_id\x18\x12 \x01(\t\x12\x1c\n\x14sell_client_order_id\x18\x13 \x01(\t\x12\x16\n\x0e\x63orrelation_id\x18\x62 \x01(\t\x12-\n\ttimestamp\x18\x63 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xb6\x02\n\x0f\x41\x64\x64TradeRequest\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\r\n\x05price\x18\x02 \x01(\x03\x12\x10\n\x08quantity\x18\x03 \x01(\x03\x12-\n\ttimestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\x0e\x61ggressor_side\x18\x05 \x01(\x0e\x32\x16.common.OrderDirection\x12\x14\n\x0c\x62uy_order_id\x18\x08 \x01(\t\x12\x15\n\rsell_order_id\x18\t \x01(\t\x12\x13\n\x0b\x62uy_user_id\x18\n \x01(\t\x12\x14\n\x0csell_user_id\x18\x0b \x01(\t\x12\x1c\n\x14\x62uyer_initial_margin\x18\x0c \x01(\x03\x12\x1d\n\x15seller_initial_margin\x18\r \x01(\x03\"\x8d\x02\n\x0bTradePublic\x12\x10\n\x08trade_id\x18\x01 \x01(\t\x12\x0e\n\x06symbol\x18\x02 \x01(\t\x12\r\n\x05price\x18\x03 \x01(\x03\x12\x10\n\x08quantity\x18\x04 \x01(\x03\x12\x33\n\x0forder_timestamp\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\x0e\x61ggressor_side\x18\x06 \x01(\x0e\x32\x16.common.OrderDirection\x12\x14\n\x0c\x62uy_order_id\x18\x08 \x01(\t\x12\x15\n\rsell_order_id\x18\t \x01(\t\x12\x13\n\x0b\x62uy_user_id\x18\n \x01(\t\x12\x14\n\x0csell_user_id\x18\x0b \x01(\t\"3\n\x0fGetTradeRequest\x12\x10\n\x08trade_id\x18\x01 \x01(\t\x12\x0e\n\x06symbol\x18\x02 \x01(\t\"2\n\x0e\x44\x65positRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0f\n\x07\x64\x65posit\x18\x02 \x01(\x03\"2\n\x13ReadBalancesRequest\x12\x0c\n\x04skip\x18\x01 \x01(\x05\x12\r\n\x05limit\x18\x02 \x01(\x05\"D\n\x0e\x42\x61lancesPublic\x12#\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x15.common.BalancePublic\x12\r\n\x05\x63ount\x18\x02 \x01(\x03\"\xe4\x02\n\x14UpdateBalanceRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x16\n\x0e\x64\x65posit_change\x18\x02 \x01(\x03\x12\x1b\n\x13realised_pnl_change\x18\x03 \x01(\x03\x12\x1b\n\x13order_margin_change\x18\x04 \x01(\x03\x12\x1e\n\x16position_margin_change\x18\x05 \x01(\x03\x12\x1d\n\x15unrealised_pnl_change\x18\x06 \x01(\x03\x12\x1a\n\x12net_funding_change\x18\x07 \x01(\x03\x12\x16\n\x0etransaction_id\x18\n \x01(\t\x12/\n\x10transaction_type\x18\x0b \x01(\x0e\x32\x15.user.TransactionType\x12\x16\n\x0e\x63orrelation_id\x18\x62 \x01(\t\x12-\n\ttimestamp\x18\x63 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"2\n\x11\x41\x64\x64\x42\x61lanceRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0c\n\x04\x63\x61sh\x18\x02 \x01(\x03\"\xa5\x01\n\x12\x43heckMarginRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0e\n\x06symbol\x18\x02 \x01(\t\x12\x14\n\x0cold_quantity\x18\x03 \x01(\x03\x12\x10\n\x08quantity\x18\x04 \x01(\x03\x12\x11\n\told_price\x18\x05 \x01(\x03\x12\r\n\x05price\x18\x06 \x01(\x03\x12$\n\x04side\x18\x07 \x01(\x0e\x32\x16.common.OrderDirection\"L\n\x13\x43heckMarginResponse\x12\x1c\n\x14is_margin_sufficient\x18\x01 \x01(\x08\x12\x17\n\x0fmargin_required\x18\x02 \x01(\x03\"z\n\x0fLeveragesPublic\x12\'\n\tleverages\x18\x01 \x03(\x0b\x32\x14.user.LeveragePublic\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12-\n\ttimestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x88\x01\n\x0eLeveragePublic\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06symbol\x18\x02 \x01(\t\x12\x16\n\x0einitial_margin\x18\x03 \x01(\x01\x12\x1a\n\x12maintenance_margin\x18\x04 \x01(\x01\x12\x14\n\x0cmax_position\x18\x05 \x01(\x03\x12\x10\n\x08leverage\x18\x06 \x01(\t\"v\n\x12SetLeverageRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0e\n\x06symbol\x18\x02 \x01(\t\x12\x10\n\x08leverage\x18\x03 \x01(\x02\x12-\n\ttimestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"J\n\x13\x41pplyFundingRequest\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12#\n\x1bnotional_value_per_quantity\x18\x02 \x01(\x03\"2\n\x0fPositionRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0e\n\x06symbol\x18\x02 \x01(\t\"\x83\x03\n\x0ePositionPublic\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06symbol\x18\x02 \x01(\t\x12\x0f\n\x07user_id\x18\x03 \x01(\t\x12\x14\n\x0cquantity_buy\x18\x04 \x01(\x03\x12\x15\n\rquantity_sell\x18\x05 \x01(\x03\x12\x11\n\tprice_buy\x18\x06 \x01(\x03\x12\x12\n\nprice_sell\x18\x07 \x01(\x03\x12\x14\n\x0cmargin_alloc\x18\x08 \x01(\x02\x12\x14\n\x0crealised_pnl\x18\t \x01(\x03\x12\x16\n\x0eunrealised_pnl\x18\n \x01(\x03\x12\x13\n\x0bnet_funding\x18\x0b \x01(\x03\x12\x17\n\x0fopen_orders_buy\x18\x0c \x01(\x03\x12\x18\n\x10open_orders_sell\x18\r \x01(\x03\x12\x19\n\x11open_quantity_buy\x18\x0e \x01(\x03\x12\x1a\n\x12open_quantity_sell\x18\x0f \x01(\x03\x12-\n\ttimestamp\x18\x63 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"s\n\x0fPositionsPublic\x12\"\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x14.user.PositionPublic\x12\r\n\x05\x63ount\x18\x02 \x01(\x03\x12-\n\ttimestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x9f\x04\n\x15UpdatePositionRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0e\n\x06symbol\x18\x02 \x01(\t\x12\x1b\n\x13quantity_buy_change\x18\x03 \x01(\x03\x12\x1c\n\x14quantity_sell_change\x18\x04 \x01(\x03\x12\x18\n\x10price_buy_change\x18\x05 \x01(\x03\x12\x19\n\x11price_sell_change\x18\x06 \x01(\x03\x12\x14\n\x0cmargin_alloc\x18\x07 \x01(\x02\x12\x1b\n\x13realised_pnl_change\x18\x08 \x01(\x03\x12\x1a\n\x12net_funding_change\x18\t \x01(\x03\x12\x1e\n\x16open_orders_buy_change\x18\n \x01(\x03\x12\x1f\n\x17open_orders_sell_change\x18\x0b \x01(\x03\x12 \n\x18open_quantity_buy_change\x18\x0c \x01(\x03\x12!\n\x19open_quantity_sell_change\x18\r \x01(\x03\x12\x10\n\x08leverage\x18\x0e \x01(\x01\x12\x16\n\x0etransaction_id\x18\x32 \x01(\t\x12/\n\x10transaction_type\x18\x33 \x01(\x0e\x32\x15.user.TransactionType\x12\x16\n\x0e\x63orrelation_id\x18\x62 \x01(\t\x12-\n\ttimestamp\x18\x63 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"E\n\x13GetUserLimitRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\r\n\x05limit\x18\x02 \x01(\x05\x12\x0e\n\x06offset\x18\x03 \x01(\x05\"\xe4\x02\n\x0bOrderPublic\x12\x10\n\x08order_id\x18\x01 \x01(\t\x12\x0e\n\x06symbol\x18\x02 \x01(\t\x12$\n\x04side\x18\x03 \x01(\x0e\x32\x16.common.OrderDirection\x12\x1f\n\x04type\x18\x04 \x01(\x0e\x32\x11.common.OrderType\x12/\n\rtime_in_force\x18\x05 \x01(\x0e\x32\x18.common.OrderTimeInForce\x12\x10\n\x08quantity\x18\x06 \x01(\x04\x12\r\n\x05price\x18\x07 \x01(\x04\x12\x0f\n\x07user_id\x18\x08 \x01(\t\x12\x17\n\x0f\x63lient_order_id\x18\t \x01(\t\x12#\n\x06status\x18\n \x01(\x0e\x32\x13.common.OrderStatus\x12\x1a\n\x12quantity_remaining\x18\x0b \x01(\x04\x12/\n\x0bupdate_time\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"o\n\x0cOrdersPublic\x12!\n\x06orders\x18\x01 \x03(\x0b\x32\x11.user.OrderPublic\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05\x63ount\x18\x03 \x01(\x05*a\n\x0fTransactionType\x12\x13\n\x0fORDER_PLACEMENT\x10\x00\x12\x16\n\x12ORDER_CANCELLATION\x10\x01\x12\x16\n\x12ORDER_MODIFICATION\x10\x02\x12\t\n\x05TRADE\x10\x03\x32\xe3\x03\n\x0bUserService\x12\x36\n\tReadUsers\x12\x16.user.ReadUsersRequest\x1a\x11.user.UsersPublic\x12\x33\n\x0cReadUserById\x12\x11.user.UserRequest\x1a\x10.user.UserPublic\x12\x30\n\x0cReadAllUsers\x12\r.common.Empty\x1a\x11.user.UsersPublic\x12\x38\n\x0fGetUserFeeGroup\x12\x11.user.UserRequest\x1a\x12.user.UserFeeGroup\x12>\n\x12GetUserMarginGroup\x12\x11.user.UserRequest\x1a\x15.user.UserMarginGroup\x12\x39\n\x0cRegisterUser\x12\x17.user.CreateUserRequest\x1a\x10.user.UserPublic\x12;\n\x13ReadUserByIdPrivate\x12\x11.user.UserRequest\x1a\x11.user.UserPrivate\x12\x43\n\x16ReadUserByEmailPrivate\x12\x16.user.UserEmailRequest\x1a\x11.user.UserPrivate2\xb5\x02\n\x0cTradeService\x12\x34\n\x08\x41\x64\x64Trade\x12\x15.user.AddTradeRequest\x1a\x11.user.TradePublic\x12\x32\n\x08GetTrade\x12\x13.common.ListRequest\x1a\x11.user.TradePublic\x12\x36\n\tGetTrades\x12\x13.common.ListRequest\x1a\x14.common.TradesPublic\x12@\n\rGetUserTrades\x12\x19.user.GetUserLimitRequest\x1a\x14.common.TradesPublic\x12\x41\n\x16GetMostRecentTradeSlow\x12\r.common.Empty\x1a\x18.user.AppendTradeRequest2\x85\x03\n\x0e\x42\x61lanceService\x12>\n\x0bGetBalances\x12\x19.user.ReadBalancesRequest\x1a\x14.user.BalancesPublic\x12\x38\n\nGetBalance\x12\x13.common.UserRequest\x1a\x15.common.BalancePublic\x12<\n\x0eGetBalanceSlow\x12\x13.common.UserRequest\x1a\x15.common.BalancePublic\x12\x38\n\x0eGetAllBalances\x12\r.common.Empty\x1a\x15.common.BalancePublic0\x01\x12\x42\n\rUpdateBalance\x12\x1a.user.UpdateBalanceRequest\x1a\x15.common.BalancePublic\x12=\n\x0e\x44\x65positBalance\x12\x14.user.DepositRequest\x1a\x15.common.BalancePublic2\x93\x01\n\x0cOrderService\x12\x43\n\x16GetMostRecentOrderSlow\x12\r.common.Empty\x1a\x1a.common.AppendOrderRequest\x12>\n\rGetUserOrders\x12\x19.user.GetUserLimitRequest\x1a\x12.user.OrdersPublic2\x9e\x02\n\rMarginService\x12\x42\n\x0b\x43heckMargin\x12\x18.user.CheckMarginRequest\x1a\x19.user.CheckMarginResponse\x12H\n\x1aGetAvailableLeverageLevels\x12\x13.common.UserRequest\x1a\x15.user.LeveragesPublic\x12=\n\x0fGetUserLeverage\x12\x13.common.UserRequest\x1a\x15.user.LeveragesPublic\x12@\n\x0fSetUserLeverage\x12\x18.user.SetLeverageRequest\x1a\x13.common.AckResponse2\xe8\x01\n\rManageService\x12\x30\n\nReloadFees\x12\r.common.Empty\x1a\x13.common.AckResponse\x12\x32\n\x0cReloadMargin\x12\r.common.Empty\x1a\x13.common.AckResponse\x12\x37\n\x11\x46lushFastBalances\x12\r.common.Empty\x1a\x13.common.AckResponse\x12\x38\n\x12\x46lushFastPositions\x12\r.common.Empty\x1a\x13.common.AckResponse2\x80\x03\n\x0fPositionService\x12:\n\x0bGetPosition\x12\x15.user.PositionRequest\x1a\x14.user.PositionPublic\x12>\n\x10GetUserPositions\x12\x13.common.UserRequest\x1a\x15.user.PositionsPublic\x12>\n\x0fGetPositionSlow\x12\x15.user.PositionRequest\x1a\x14.user.PositionPublic\x12=\n\x0e\x43reatePosition\x12\x15.user.PositionRequest\x1a\x14.user.PositionPublic\x12\x38\n\x0fGetAllPositions\x12\r.common.Empty\x1a\x14.user.PositionPublic0\x01\x12\x38\n\x0c\x41pplyFunding\x12\x19.user.ApplyFundingRequest\x1a\r.common.Emptyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TRANSACTIONTYPE']._serialized_start=4968
  _globals['_TRANSACTIONTYPE']._serialized_end=5065
  _globals['_USERREQUEST']._serialized_start=67
  _globals['_USERREQUEST']._serialized_end=97
  _globals['_USEREMAILREQUEST']._serialized_start=99
  _globals['_USEREMAILREQUEST']._serialized_end=132
  _globals['_USERFEEGROUP']._serialized_start=134
  _globals['_USERFEEGROUP']._serialized_end=187
  _globals['_USERMARGINGROUP']._serialized_start=189
  _globals['_USERMARGINGROUP']._serialized_end=248
  _globals['_USERPUBLIC']._serialized_start=251
  _globals['_USERPUBLIC']._serialized_end=391
  _globals['_USERPRIVATE']._serialized_start=394
  _globals['_USERPRIVATE']._serialized_end=595
  _globals['_USERSPUBLIC']._serialized_start=597
  _globals['_USERSPUBLIC']._serialized_end=657
  _globals['_CREATEUSERREQUEST']._serialized_start=659
  _globals['_CREATEUSERREQUEST']._serialized_end=730
  _globals['_USERCREATERESPONSE']._serialized_start=732
  _globals['_USERCREATERESPONSE']._serialized_end=784
  _globals['_READUSERSREQUEST']._serialized_start=786
  _globals['_READUSERSREQUEST']._serialized_end=833
  _globals['_APPENDTRADEREQUEST']._serialized_start=836
  _globals['_APPENDTRADEREQUEST']._serialized_end=1390
  _globals['_ADDTRADEREQUEST']._serialized_start=1393
  _globals['_ADDTRADEREQUEST']._serialized_end=1703
  _globals['_TRADEPUBLIC']._serialized_start=1706
  _globals['_TRADEPUBLIC']._serialized_end=1975
  _globals['_GETTRADEREQUEST']._serialized_start=1977
  _globals['_GETTRADEREQUEST']._serialized_end=2028
  _globals['_DEPOSITREQUEST']._serialized_start=2030
  _globals['_DEPOSITREQUEST']._serialized_end=2080
  _globals['_READBALANCESREQUEST']._serialized_start=2082
  _globals['_READBALANCESREQUEST']._serialized_end=2132
  _globals['_BALANCESPUBLIC']._serialized_start=2134
  _globals['_BALANCESPUBLIC']._serialized_end=2202
  _globals['_UPDATEBALANCEREQUEST']._serialized_start=2205
  _globals['_UPDATEBALANCEREQUEST']._serialized_end=2561
  _globals['_ADDBALANCEREQUEST']._serialized_start=2563
  _globals['_ADDBALANCEREQUEST']._serialized_end=2613
  _globals['_CHECKMARGINREQUEST']._serialized_start=2616
  _globals['_CHECKMARGINREQUEST']._serialized_end=2781
  _globals['_CHECKMARGINRESPONSE']._serialized_start=2783
  _globals['_CHECKMARGINRESPONSE']._serialized_end=2859
  _globals['_LEVERAGESPUBLIC']._serialized_start=2861
  _globals['_LEVERAGESPUBLIC']._serialized_end=2983
  _globals['_LEVERAGEPUBLIC']._serialized_start=2986
  _globals['_LEVERAGEPUBLIC']._serialized_end=3122
  _globals['_SETLEVERAGEREQUEST']._serialized_start=3124
  _globals['_SETLEVERAGEREQUEST']._serialized_end=3242
  _globals['_APPLYFUNDINGREQUEST']._serialized_start=3244
  _globals['_APPLYFUNDINGREQUEST']._serialized_end=3318
  _globals['_POSITIONREQUEST']._serialized_start=3320
  _globals['_POSITIONREQUEST']._serialized_end=3370
  _globals['_POSITIONPUBLIC']._serialized_start=3373
  _globals['_POSITIONPUBLIC']._serialized_end=3760
  _globals['_POSITIONSPUBLIC']._serialized_start=3762
  _globals['_POSITIONSPUBLIC']._serialized_end=3877
  _globals['_UPDATEPOSITIONREQUEST']._serialized_start=3880
  _globals['_UPDATEPOSITIONREQUEST']._serialized_end=4423
  _globals['_GETUSERLIMITREQUEST']._serialized_start=4425
  _globals['_GETUSERLIMITREQUEST']._serialized_end=4494
  _globals['_ORDERPUBLIC']._serialized_start=4497
  _globals['_ORDERPUBLIC']._serialized_end=4853
  _globals['_ORDERSPUBLIC']._serialized_start=4855
  _globals['_ORDERSPUBLIC']._serialized_end=4966
  _globals['_USERSERVICE']._serialized_start=5068
  _globals['_USERSERVICE']._serialized_end=5551
  _globals['_TRADESERVICE']._serialized_start=5554
  _globals['_TRADESERVICE']._serialized_end=5863
  _globals['_BALANCESERVICE']._serialized_start=5866
  _globals['_BALANCESERVICE']._serialized_end=6255
  _globals['_ORDERSERVICE']._serialized_start=6258
  _globals['_ORDERSERVICE']._serialized_end=6405
  _globals['_MARGINSERVICE']._serialized_start=6408
  _globals['_MARGINSERVICE']._serialized_end=6694
  _globals['_MANAGESERVICE']._serialized_start=6697
  _globals['_MANAGESERVICE']._serialized_end=6929
  _globals['_POSITIONSERVICE']._serialized_start=6932
  _globals['_POSITIONSERVICE']._serialized_end=7316
# @@protoc_insertion_point(module_scope)
