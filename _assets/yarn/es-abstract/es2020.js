'use strict';

/* eslint global-require: 0 */
// https://ecma-international.org/ecma-262/11.0/#sec-abstract-operations
var ES2020 = {
	'Abstract Equality Comparison': require('./2020/AbstractEqualityComparison'),
	'Abstract Relational Comparison': require('./2020/AbstractRelationalComparison'),
	'Strict Equality Comparison': require('./2020/StrictEqualityComparison'),
	abs: require('./2020/abs'),
	AddEntriesFromIterable: require('./2020/AddEntriesFromIterable'),
	AdvanceStringIndex: require('./2020/AdvanceStringIndex'),
	ArrayCreate: require('./2020/ArrayCreate'),
	ArraySetLength: require('./2020/ArraySetLength'),
	ArraySpeciesCreate: require('./2020/ArraySpeciesCreate'),
	BigIntBitwiseOp: require('./2020/BigIntBitwiseOp'),
	BinaryAnd: require('./2020/BinaryAnd'),
	BinaryOr: require('./2020/BinaryOr'),
	BinaryXor: require('./2020/BinaryXor'),
	Call: require('./2020/Call'),
	CanonicalNumericIndexString: require('./2020/CanonicalNumericIndexString'),
	CodePointAt: require('./2020/CodePointAt'),
	CompletePropertyDescriptor: require('./2020/CompletePropertyDescriptor'),
	CopyDataProperties: require('./2020/CopyDataProperties'),
	CreateDataProperty: require('./2020/CreateDataProperty'),
	CreateDataPropertyOrThrow: require('./2020/CreateDataPropertyOrThrow'),
	CreateHTML: require('./2020/CreateHTML'),
	CreateIterResultObject: require('./2020/CreateIterResultObject'),
	CreateListFromArrayLike: require('./2020/CreateListFromArrayLike'),
	CreateMethodProperty: require('./2020/CreateMethodProperty'),
	DateFromTime: require('./2020/DateFromTime'),
	DateString: require('./2020/DateString'),
	Day: require('./2020/Day'),
	DayFromYear: require('./2020/DayFromYear'),
	DaysInYear: require('./2020/DaysInYear'),
	DayWithinYear: require('./2020/DayWithinYear'),
	DefinePropertyOrThrow: require('./2020/DefinePropertyOrThrow'),
	DeletePropertyOrThrow: require('./2020/DeletePropertyOrThrow'),
	EnumerableOwnPropertyNames: require('./2020/EnumerableOwnPropertyNames'),
	FlattenIntoArray: require('./2020/FlattenIntoArray'),
	floor: require('./2020/floor'),
	FromPropertyDescriptor: require('./2020/FromPropertyDescriptor'),
	Get: require('./2020/Get'),
	GetIterator: require('./2020/GetIterator'),
	GetMethod: require('./2020/GetMethod'),
	GetOwnPropertyKeys: require('./2020/GetOwnPropertyKeys'),
	GetPrototypeFromConstructor: require('./2020/GetPrototypeFromConstructor'),
	GetSubstitution: require('./2020/GetSubstitution'),
	GetV: require('./2020/GetV'),
	HasOwnProperty: require('./2020/HasOwnProperty'),
	HasProperty: require('./2020/HasProperty'),
	HourFromTime: require('./2020/HourFromTime'),
	InLeapYear: require('./2020/InLeapYear'),
	InstanceofOperator: require('./2020/InstanceofOperator'),
	Invoke: require('./2020/Invoke'),
	IsAccessorDescriptor: require('./2020/IsAccessorDescriptor'),
	IsArray: require('./2020/IsArray'),
	IsBigIntElementType: require('./2020/IsBigIntElementType'),
	IsCallable: require('./2020/IsCallable'),
	IsConcatSpreadable: require('./2020/IsConcatSpreadable'),
	IsConstructor: require('./2020/IsConstructor'),
	IsDataDescriptor: require('./2020/IsDataDescriptor'),
	IsExtensible: require('./2020/IsExtensible'),
	IsGenericDescriptor: require('./2020/IsGenericDescriptor'),
	IsInteger: require('./2020/IsInteger'),
	IsNonNegativeInteger: require('./2020/IsNonNegativeInteger'),
	IsNoTearConfiguration: require('./2020/IsNoTearConfiguration'),
	IsPromise: require('./2020/IsPromise'),
	IsPropertyKey: require('./2020/IsPropertyKey'),
	IsRegExp: require('./2020/IsRegExp'),
	IsStringPrefix: require('./2020/IsStringPrefix'),
	IsUnclampedIntegerElementType: require('./2020/IsUnclampedIntegerElementType'),
	IsUnsignedElementType: require('./2020/IsUnsignedElementType'),
	IterableToList: require('./2020/IterableToList'),
	IteratorClose: require('./2020/IteratorClose'),
	IteratorComplete: require('./2020/IteratorComplete'),
	IteratorNext: require('./2020/IteratorNext'),
	IteratorStep: require('./2020/IteratorStep'),
	IteratorValue: require('./2020/IteratorValue'),
	LengthOfArrayLike: require('./2020/LengthOfArrayLike'),
	MakeDate: require('./2020/MakeDate'),
	MakeDay: require('./2020/MakeDay'),
	MakeTime: require('./2020/MakeTime'),
	MinFromTime: require('./2020/MinFromTime'),
	modulo: require('./2020/modulo'),
	MonthFromTime: require('./2020/MonthFromTime'),
	msFromTime: require('./2020/msFromTime'),
	NumberBitwiseOp: require('./2020/NumberBitwiseOp'),
	OrdinaryCreateFromConstructor: require('./2020/OrdinaryCreateFromConstructor'),
	OrdinaryDefineOwnProperty: require('./2020/OrdinaryDefineOwnProperty'),
	OrdinaryGetOwnProperty: require('./2020/OrdinaryGetOwnProperty'),
	OrdinaryGetPrototypeOf: require('./2020/OrdinaryGetPrototypeOf'),
	OrdinaryHasInstance: require('./2020/OrdinaryHasInstance'),
	OrdinaryHasProperty: require('./2020/OrdinaryHasProperty'),
	OrdinaryObjectCreate: require('./2020/OrdinaryObjectCreate'),
	OrdinarySetPrototypeOf: require('./2020/OrdinarySetPrototypeOf'),
	PromiseResolve: require('./2020/PromiseResolve'),
	QuoteJSONString: require('./2020/QuoteJSONString'),
	RegExpExec: require('./2020/RegExpExec'),
	RequireObjectCoercible: require('./2020/RequireObjectCoercible'),
	SameValue: require('./2020/SameValue'),
	SameValueNonNumeric: require('./2020/SameValueNonNumeric'),
	SameValueZero: require('./2020/SameValueZero'),
	SecFromTime: require('./2020/SecFromTime'),
	Set: require('./2020/Set'),
	SetFunctionLength: require('./2020/SetFunctionLength'),
	SetFunctionName: require('./2020/SetFunctionName'),
	SetIntegrityLevel: require('./2020/SetIntegrityLevel'),
	SpeciesConstructor: require('./2020/SpeciesConstructor'),
	StringGetOwnProperty: require('./2020/StringGetOwnProperty'),
	StringPad: require('./2020/StringPad'),
	SymbolDescriptiveString: require('./2020/SymbolDescriptiveString'),
	TestIntegrityLevel: require('./2020/TestIntegrityLevel'),
	thisBigIntValue: require('./2020/thisBigIntValue'),
	thisBooleanValue: require('./2020/thisBooleanValue'),
	thisNumberValue: require('./2020/thisNumberValue'),
	thisStringValue: require('./2020/thisStringValue'),
	thisSymbolValue: require('./2020/thisSymbolValue'),
	thisTimeValue: require('./2020/thisTimeValue'),
	TimeClip: require('./2020/TimeClip'),
	TimeFromYear: require('./2020/TimeFromYear'),
	TimeString: require('./2020/TimeString'),
	TimeWithinDay: require('./2020/TimeWithinDay'),
	ToBoolean: require('./2020/ToBoolean'),
	ToDateString: require('./2020/ToDateString'),
	ToIndex: require('./2020/ToIndex'),
	ToInt16: require('./2020/ToInt16'),
	ToInt32: require('./2020/ToInt32'),
	ToInt8: require('./2020/ToInt8'),
	ToInteger: require('./2020/ToInteger'),
	ToLength: require('./2020/ToLength'),
	ToNumber: require('./2020/ToNumber'),
	ToNumeric: require('./2020/ToNumeric'),
	ToObject: require('./2020/ToObject'),
	ToPrimitive: require('./2020/ToPrimitive'),
	ToPropertyDescriptor: require('./2020/ToPropertyDescriptor'),
	ToPropertyKey: require('./2020/ToPropertyKey'),
	ToString: require('./2020/ToString'),
	ToUint16: require('./2020/ToUint16'),
	ToUint32: require('./2020/ToUint32'),
	ToUint8: require('./2020/ToUint8'),
	ToUint8Clamp: require('./2020/ToUint8Clamp'),
	TrimString: require('./2020/TrimString'),
	Type: require('./2020/Type'),
	UnicodeEscape: require('./2020/UnicodeEscape'),
	UTF16DecodeString: require('./2020/UTF16DecodeString'),
	UTF16DecodeSurrogatePair: require('./2020/UTF16DecodeSurrogatePair'),
	UTF16Encoding: require('./2020/UTF16Encoding'),
	ValidateAndApplyPropertyDescriptor: require('./2020/ValidateAndApplyPropertyDescriptor'),
	WeekDay: require('./2020/WeekDay'),
	YearFromTime: require('./2020/YearFromTime')
};

module.exports = ES2020;
